class Election:
    def __init__(self):
        self._contestants = list()
        self._reported_results = list()
        self._ballots = list()

    def get_contestants(self):
        return self._contestants

    def set_contestants(self, contestants):
        self._contestants = contestants

    def get_reported_results(self):
        return self._reported_results

    def set_reported_results(self, reported_results):
        self._reported_results = reported_results

    def get_ballots(self):
        return self._ballots

    def set_ballots(self, ballots):
        self._ballots = ballots

    def get_ballot(self, index):
        return self._ballots[index]

    def add_ballot(self, ballot):
        self._ballots.append(ballot)

    def get_ballot_count(self):
        return len(self._ballots)
