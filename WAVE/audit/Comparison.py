from math import log, ceil
import audit
import election

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
        self._cached_results = list()
        self._ballot_count = list()

    def init(self, results, ballot_count):
        self._status = 0
        self._cached_results = list()
        self._ballot_count = ballot_count

        self._o1 = 0
        self._o2 = 0
        self._u1 = 0
        self._u2 = 0

        results_sorted = sorted(results,
                                key=lambda r: r.get_percentage(),
                                reverse=True)

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

    def get_progress(self):
        return "{} correct \nballots left".format(self._stopping_count)

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

    def compute(self, ballot):
        # Flag if the stopping count needs to be recomputed mathematically
        recompute = True

        # No discrepency in the ballot
        if ballot.get_actual_value() == ballot.get_reported_value():
            self._stopping_count -= 1
            recompute = False

        # If the ballot is an undervote
        if ballot.get_reported_value().get_id() == election.Undervote.CID:
            if ballot.get_actual_value().equals(self._winner):
                self._u1 += 1
            else:
                self._o1 += 1

        # If the ballot is an overvote
        elif ballot.get_reported_value().get_id() == election.Overvote.CID:
            if ballot.get_actual_value().equals(self._winner):
                self._u1 += 1
            else:
                self._ol += 1

        # If the ballot is a reported vote for the winner, but is really a vote for the
        # loser
        elif ballot.get_reported_value().equals(self._winner) and \
                not ballot.get_actual_value().equals(self._winner):
            self._o2 += 1

        # If the ballot is a reported vote for a loser, but is really a vote for the 
        # winner
        elif not ballot.get_reported_value().equals(self._winner) and \
                ballot.get_actual_value().equals(self._winner):
            self._u2 += 1

        # Error handling
        elif recompute:
            print("Error processing ballot {}".format(ballot.get_physical_ballot_num()))
            print("Actual: {}".format(ballot.get_actual_value().get_name()))
            print("Reported: {}".format(ballot.get_reported_value().get_name()))

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
        self.init(results, self._ballot_count)

        for ballot in ballots:
            self.compute(ballot)
            
            if self._stopping_count == 0:
                return ballot

    def get_current_result(self):
        count = 0

        for result in self._cached_results:
            count += result[1]

        audit_results = []

        for person in self._cached_results:
            result = election.Result(person[0], person[1] / count)
            audit_results.append(result)
