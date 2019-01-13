from math import log, ceil
import audit
import election
import numpy as np
import os

os.sys.path.append("2018-bctool/code/")
import bctool


"""
Based off of Dr. Stark's "Super-Simple Simultaneous Single-ballot Risk Limiting Audits"
"""

class Comparison(audit.Audit):
    name = "Comparison RLA"
    status_codes = ["In Progress",
                    "Election Results \nVerified"]

    def __init__(self):
        # Arbritary Starting Numbers - taken from Stark's paper
        self._risk_limit = 0.05
        self._inflator = 1.03905
        self._o1_expected = 0.001
        self._o2_expected = 0.0001
        self._u1_expected = 0.001
        self._u2_expected = 0.0001

        self._o1 = 0
        self._o2 = 0
        self._u1 = 0
        self._u2 = 0
        self._stopping_count = 0
        self._diluted_margin = 0
        self._status = 0

        self._winner = None
        self._candidates = None
        self.upset_prob = None
        self._cached_results = list()
        self._ballot_count = list()
        self._reported_choices = dict()

    def init(self, results, ballot_count, reported_choices):
        self._status = 0
        self._cached_results = list()
        self._ballot_count = ballot_count
        self._reported_choices = reported_choices
        self._o1 = 0
        self._o2 = 0
        self._u1 = 0
        self._u2 = 0

        results_sorted = sorted(results,
                                key=lambda r: r.get_percentage(),
                                reverse=True)

        self._candidates = []
        for r in results_sorted:
            self._candidates.append(r.get_contestant().get_name())
        self._candidates.extend(["overvote", "undervote", "Write-in"])

        self.bayesian_formatted_results = {k: {} for k in self._candidates}
        for candidate in self.bayesian_formatted_results:
            # This is a dict of dicts, where self.bayesian_formatted_results[i][j] is the number
            # of votes that were reported for i and were actually for j
            self.bayesian_formatted_results[candidate] = {j: 0 for j in self._candidates}

        self._winner = results_sorted[0].get_contestant()

        margin = results_sorted[0].get_votes() - results_sorted[1].get_votes()
        self._diluted_margin = margin / self._ballot_count
        self._stopping_count = ceil(-2 * self._inflator * log(self._risk_limit) / ( \
                self._diluted_margin + 2 * self._inflator * ( \
                    self._o1_expected * log(1 - (1 / (2 * self._inflator))) + \
                    self._o2_expected * log(1 - (1 / self._inflator)) + \
                    self._u1_expected * log(1 + (1 / (2 * self._inflator))) + \
                    self._u2_expected * log(1 + (1 / self._inflator))
                    )
                ))

        print("Results:")
        
        for r in results_sorted:
            print("Contestant: {}".format(r.get_contestant().get_name()))
            print("Votes: {}".format(r.get_votes()))

        print("Initial Stopping Count: {}".format(self._stopping_count))
        print("Margin: {}".format(margin))
        print("Total Votes: {}".format(self._ballot_count))
        print("Diluted Margin: {}".format(self._diluted_margin))
        print("Risk Limit: {}".format(self._risk_limit))

        for result in results:
            self._cached_results.append([result.get_contestant(), 0])

    def get_progress(self, final=False):
        progress_str = ""
        if final:
            progress_str += "{} correct \nballots left; Upset probability={} \n".format(self._stopping_count, self.upset_prob)
        for actual_candidate in self._candidates:
            for reported_candidate in self._candidates:
                count = self.bayesian_formatted_results[reported_candidate][actual_candidate]
                if count != 0:
                    progress_str += "Actual votes for {} reported in CVR for {}: {} \n".format(actual_candidate, reported_candidate,count)
        return progress_str

    def get_status(self):
        return Comparison.status_codes[self._status]

    @staticmethod
    def get_name():
        return Comparison.name

    def get_parameters(self):
        param = [["Risk Limit", str(self._risk_limit * 100)],
                 ["Error Inflation Factor", str(self._inflator)],
                 ["Expected 1-vote Overstatement Rate", str(self._o1_expected)],
                 ["Expected 2-vote Overstatement Rate", str(self._o2_expected)],
                 ["Expected 1-vote Understatement Rate", str(self._u1_expected)],
                 ["Expected 2-vote Understatement Rate", str(self._u2_expected)]]

        return param

    def set_parameters(self, param):
        self._risk_limit = float(param[0]) / 100
        self._inflator = float(param[1])
        self._o1_expected = float(param[2])
        self._o2_expected = float(param[3])
        self._u1_expected = float(param[4])
        self._u2_expected = float(param[5])

    def compute_upset_prob(self, seed=1, num_trials=10000, n_winners=1):
        strata = []
        strata_sizes = []
        print(self._reported_choices)
        for reported in self._reported_choices:
            strata.append(("Total", reported))
            strata_sizes.append(self._reported_choices[reported])


        strata_sample_tallies = []
        strata_pseudocounts = []
        for (collection, reported_choice) in strata:
            stratum_sample_tally = []
            stratum_pseudocounts = []
            for actual_choice in self._candidates:
                stratum_sample_tally.append(self.bayesian_formatted_results[reported_choice][actual_choice])
                if reported_choice == actual_choice:
                    stratum_pseudocounts.append(5)
                else:
                    stratum_pseudocounts.append(1)
            strata_sample_tallies.append(np.array(stratum_sample_tally))
            strata_pseudocounts.append(np.array(stratum_pseudocounts))
        win_probs = bctool.compute_win_probs(strata_sample_tallies,
                                       strata_pseudocounts,
                                       strata_sizes,
                                       seed,
                                       num_trials,
                                       self._candidates,
                                       n_winners)
        self.upset_prob = 1.0 - win_probs[0][1]
        print(win_probs)

    def is_ballot_invalid(self, ballot):
        return ballot.get_actual_value().get_id() == election.Undervote.CID or ballot.get_actual_value().get_id() == election.Overvote.CID


    def compute(self, ballot):
        # Flag if the stopping count needs to be recomputed mathematically
        recompute = True

        actual_name = ballot.get_actual_value().get_name()
        reported_name = ballot.get_reported_value().get_name()
        self.bayesian_formatted_results[reported_name][actual_name] += 1

        total_num_candidates = len(self._candidates)
        if "undervote" in self._candidates:
            total_num_candidates -= 1
        if "overvote" in self._candidates:
            total_num_candidates -= 1

        # No discrepency in the ballot
        if ballot.get_actual_value() == ballot.get_reported_value():
            self._stopping_count -= 1
            recompute = False
        # If the ballot is reported as an undervote or an overvote
        elif ballot.get_reported_value().get_id() == election.Undervote.CID or ballot.get_reported_value().get_id() == election.Overvote.CID:
            # if actual is for winner, is 1-vote U
            if ballot.get_actual_value().equals(self._winner):
                self._u1 += 1
            # if actual is for a valid loser, is 1-vote O
            elif not self.is_ballot_invalid(ballot):
                self._o1 += 1
        # If reported is for winner:
        elif ballot.get_reported_value().equals(self._winner):
            # if actual is invalid, 1-vote O
            if self.is_ballot_invalid(ballot):
                self._o1 += 1
            # if actual is for loser is 2-vote O
            else:
                self._o2 += 1

        # If the ballot is a reported vote for a loser
        elif not ballot.get_reported_value().equals(self._winner):
            if not self.is_ballot_invalid(ballot):
                # if actual is for winner, is 1-vote U
                if ballot.get_actual_value().equals(self._winner):
                    # In a 2-candidate election, this is a 2-vote understatement
                    if total_num_candidates == 2:
                        self._u2 += 1
                    # if multiple candidates, this is a 1-vote understatement
                    else:
                        self._u1 += 1
                # if reported is for different loser, is 1-vote O
                else:
                    self._o1 += 1
        # Error handling
        elif recompute:
            print("Error processing ballot {}".format(ballot.get_physical_ballot_num()))
            print("Actual: {}".format(ballot.get_actual_value().get_name()))
            print("Reported: {}".format(ballot.get_reported_value().get_name()))
        print("u1={},o1={},u2={},o2={}".format(self._u1,self._o1,self._u2,self._o2))
        # Recacluate count using Stark's formula
        if recompute:
            self._stopping_count = ceil(-2 * self._inflator * ( \
                    log(self._risk_limit) + \
                    self._o1 * log(1 - 1 / (2 * self._inflator)) + \
                    self._o2 * log(1 - 1 / self._inflator) + \
                    self._u1 * log(1 + 1 / (2 * self._inflator)) + \
                    self._u2 * log(1 + 1 / self._inflator)) \
                    / self._diluted_margin)

        # Update cached results
        for i in range(len(self._cached_results)):
            if self._cached_results[i][0].equals(ballot.get_actual_value()):
                self._cached_results[i][1] += 1
                break

        # Update status
        self._refresh_status()

        # print("\n")
        # print("Ballot {}".format(ballot.get_audit_seq_num()))
        # print("Actual: {}".format(ballot.get_actual_value().get_name()))
        # print("Reported: {}".format(ballot.get_reported_value().get_name()))
        # print("Stopping Count: {}".format(self._stopping_count))

    def _refresh_status(self):
        if self._stopping_count == 0:
            self._status = 1
        else:
            self._status = 0

    def recompute(self, ballots, results):
        self.init(results, self._ballot_count, self._reported_choices)

        for ballot in ballots:
            self.compute(ballot)
            
            if self._stopping_count == 0:
                return ballot
        self.compute_upset_prob()

    def get_current_result(self):
        count = 0

        for result in self._cached_results:
            count += result[1]

        audit_results = []

        for person in self._cached_results:
            result = election.Result(person[0], person[1] / count)
            audit_results.append(result)
