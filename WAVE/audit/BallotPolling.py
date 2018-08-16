import audit
import election


class BallotPolling(audit.Audit):
    name = "Ballot Polling Audit"
    status_codes = ["In Progress", 
                    "Election Results Verified",
                    "Full Hand Count Required"]

    def __init__(self):
        self._T = 1
        self._s = -1
        self._margin = -1
        self._winner = -1
        self._tolerance = .01

        self._status = 0
        self._cached_results = list()
        self._ballot_count = None

    def init(self, results, ballot_count):
        self._T = 1
        self._s = -1
        self._margin = -1
        self._winner = None

        self._status = 0
        self._cached_results = list()

        results_sorted = sorted(results, 
                                key=lambda r: r.get_percentage(),
                                reverse=True)

        self._s = results_sorted[0].get_percentage()
        self._winner = results_sorted[0].get_contestant()
        self._margin = self._s - self._tolerance

        self._ballot_count = ballot_count

        for result in results:
            self._cached_results.append([result.get_contestant(), 0])

        print("Winner: {}".format(self._winner.get_name()))
        print("Init T: {}".format(self._T))
        print("Init Margin: {}".format(self._margin))

    def get_progress(self):
        return "T = {0:.4f}".format(self._T)

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

    def compute(self, ballot):
        ballot_vote = ballot.get_actual_value()

        if ballot_vote.equals(self._winner):
            self._T *= self._margin / .50
        else:
            self._T *= (1 - self._margin) / .50

        for i in range(len(self._cached_results)):
            if self._cached_results[i][0].equals(ballot_vote):
                self._cached_results[i][1] += 1
                break

        # print(str(self._T) + " " + ballot.get_reported_value().get_name() + " " + ballot.get_actual_value().get_name())

        self._refresh_status()

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

            if self._T > 9.9 or self._T < 0.011:
                return ballot

    def get_current_result(self):
        count = 0

        for result in self._cached_results:
            count += result[1]

        audit_results = []

        for person in self._cached_results:
            result = election.Result(person[0], person[1] / count)
            audit_results.append(result)

        return audit_results
