import audit
import election
import numpy as np
import os

os.sys.path.append("2018-bctool/code/")
import bctool


class BallotPolling(audit.Audit):
    name = "Ballot Polling Audit"
    status_codes = ["In Progress", 
                    "Election Results Verified",
                    "Full Hand Count Required"]

    def __init__(self):
        self._T = 1
        self._s = -1
        self._m = 0
        self._s_wl = {}
        self._t_loser = {}
        self._winner = -1
        self._tolerance = .01
        self._status = 0
        self._cached_results = list()
        self._ballot_count = None
        self.upset_prob = None

    def init(self, results, ballot_count):
        self._T = 1
        self._s = -1
        self._m = 0
        self._s_wl = {}
        self._t_loser = {}
        self._winner = None
        self.upset_prob = None
        self._status = 0

        results_sorted = sorted(results, 
                                key=lambda r: r.get_percentage(),
                                reverse=True)

        self._candidates = []
        for r in results_sorted:
            self._candidates.append(r.get_contestant().get_name())
        self._candidates.extend(["overvote", "undervote", "Write-in"])

        self._s = results_sorted[0].get_percentage()
        self._winner = results_sorted[0].get_contestant()
        #self._margin = self._s - self._tolerance

        self.loser_names = [r.get_contestant().get_name() for r in results_sorted if r != results_sorted[0]]
        #dictionary of T values for losing canddidates
        #   usage: self._t_winner_loser[losing_candidate]
        self._t_loser = {lose_c : 1 for lose_c in self.loser_names}

        #dictionary of (losing) candidate to votes for winner / (total votes for either)
        #    s_wl from BRAVO paper
        #    usage self._s_wl[losing_candidate]
        self._s_wl =  {r.get_contestant()._name : self._s / (r.get_percentage() + self._s) for r in results_sorted if r.get_contestant() != self._winner}

        self._ballot_count = ballot_count

        for result in results:
            self._cached_results.append([result.get_contestant(), 0])
        # assert(False)
        self.bayesian_formatted_results = {k: 0 for k in self._candidates}

        print("Winner: {}".format(self._winner.get_name()))
        print("Init T values : {}".format(self._t_loser))
        print("Initial s_wl values: {}".format(self._s_wl))

    def get_progress(self, final=False):
        progress_str = ""
        if final:
            progress_str += "T Winner {} vs candidate values = {}; upset_prob = {} \n".format(self._winner.get_name(), self._t_loser, self.upset_prob)
        progress_str += "Current results: \n {}".format(self.bayesian_formatted_results)
        return progress_str

    def get_status(self):
       return BallotPolling.status_codes[self._status]

    @staticmethod
    def get_name():
        return BallotPolling.name

    def get_parameters(self):
        param = [["Tolerance", "{0:.2f}%".format(self._tolerance * 100)]]
        return param

    def set_parameters(self, param):
        if isinstance(param[0], int):
            self._tolerance = float(param[0]) / 100
        else:
            self._tolerance = float(param[0].replace("%", "")) / 100


    def is_ballot_invalid(self, ballot):
        return ballot.get_actual_value().get_id() == election.Undervote.CID or ballot.get_actual_value().get_id() == election.Overvote.CID

    def compute(self, ballot):
        ballot_vote = ballot.get_actual_value()
        ballot_name = ballot_vote.get_name()
        winner_name = self._winner.get_name()

        self.bayesian_formatted_results[ballot_vote.get_name()] += 1
        # Vote for reported winner
        if ballot_name == winner_name:
            for lose_c in self.loser_names :
                # multiply Twl by sw`/0.5.
                self._t_loser[lose_c] = 2 * self._t_loser[lose_c] * self._s_wl[lose_c]
        # Vote for reported loser
        elif not self.is_ballot_invalid(ballot):
            self._t_loser[ballot_name]  = 2 *  self._t_loser[ballot_name] * (1-self._s_wl[ballot_name])

        else:
            print("T is not updated since ballot was invalid")

        for i in range(len(self._cached_results)):
            if self._cached_results[i][0].equals(ballot_vote):
                self._cached_results[i][1] += 1
                break

        print("Vote for: %s winner: %s update T: %s " % (ballot_name, winner_name, str(self._t_loser)))
        # print(str(self._T) + " " + ballot.get_reported_value().get_name() + " " + ballot.get_actual_value().get_name())

        self._refresh_status()

    def compute_upset_prob(self, seed=1, num_trials=10000, n_winners=1):
        strata = [("Total", "-Missing")]
        total_num_votes = [self._ballot_count]
        strata_sample_tallies = []
        strata_pseudocounts = []
        for (collection, reported_choice) in strata:
            stratum_sample_tally = []
            stratum_pseudocounts = []
            for actual_choice in self._candidates:
                stratum_sample_tally.append(self.bayesian_formatted_results[actual_choice])
                if reported_choice == actual_choice:
                    stratum_pseudocounts.append(50)
                else:
                    stratum_pseudocounts.append(1)
        strata_sample_tallies.append(np.array(stratum_sample_tally))
        strata_pseudocounts.append(np.array(stratum_pseudocounts))
        win_probs = bctool.compute_win_probs(strata_sample_tallies,
                                       strata_pseudocounts,
                                       total_num_votes,
                                       seed,
                                       num_trials,
                                       self._candidates,
                                       n_winners)

        self.upset_prob = 1.0 - win_probs[0][1]

    def _refresh_status(self):
        if self._T > 9.9:
            self._status = 1
        elif self._T < 0.011:
            self._status = 2
        else:
            self._status = 0

    def recompute(self, ballots, results):
        self.init(results, self._ballot_count)

        for ballot in ballots:
            self.compute(ballot)

            self.compute_upset_prob()
            #TODO: if T reject null hypothesis do not update TL


    def update_reported_ballots(self, ballots, results):
        self.init(results, self._ballot_count)
        for ballot in ballots:
            self.compute(ballot)

    def get_current_result(self):
        count = 0

        for result in self._cached_results:
            count += result[1]

        audit_results = []

        for person in self._cached_results:
            result = election.Result(person[0], person[1] / count)
            audit_results.append(result)

        return audit_results
