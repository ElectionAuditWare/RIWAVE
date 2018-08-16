import math
from random import shuffle, choice
import election


class Pres2016:
    def __init__(self):
        self._election = election.Election()

        self._gen_and_set_candidates()
        self._set_reported_results()

    def get_election(self): 
        return self._election
    
    def _gen_and_set_candidates(self):
        self._contestants = []

        self._contestants.append(election.Contestant(0, "Hillary Clinton"))
        self._contestants.append(election.Contestant(1, "Donald J. Trump"))
        self._contestants.append(election.Contestant(2, "Gary Johnson"))
        self._contestants.append(election.Contestant(3, "Write In"))
        self._contestants.append(election.Contestant(4, "Jill Stein"))
        self._contestants.append(election.Contestant(5, "Roque De La Fuente"))

        self._election.set_contestants(self._contestants)

    def _set_reported_results(self):
        self._results = []

        self._results.append(election.Result(self._contestants[0], .544))
        self._results.append(election.Result(self._contestants[1], 0.389))
        self._results.append(election.Result(self._contestants[2], 0.032))
        self._results.append(election.Result(self._contestants[3], 0.02))
        self._results.append(election.Result(self._contestants[4], 0.013))
        self._results.append(election.Result(self._contestants[5], 0.001))
        
        self._election.set_reported_results(self._results)

    def get_reported_results(self):
        return self._results

    def gen_ballots(self, count, error):
        sorted_results = sorted(self._results, 
                                key=lambda r: r.get_percentage(),
                                reverse=True)

        ballots = []
        audit_counts = [i for i in range(count)]

        for i, result in enumerate(sorted_results):
            for j in range(int(result.get_percentage() * count)):
                current_count = choice(audit_counts)
                audit_counts.remove(current_count)

                ballot = election.Ballot()

                ballot.set_physical_ballot_num(current_count)
                ballot.set_reported_value(result.get_contestant())

                if i == 0 and j < error * result.get_percentage() * count:
                    ballot.set_actual_value(sorted_results[i + 1].get_contestant())
                else:
                    ballot.set_actual_value(result.get_contestant())

                ballots.append(ballot)
                
                for r in self._results:
                    if r.get_contestant() == ballot.get_reported_value():
                        r.set_votes(r.get_votes() + 1)
                        break

        shuffle(ballots)
        shuffle(ballots)
        shuffle(ballots)

        for i, ballot in enumerate(ballots):
            ballot.set_audit_seq_num(i)

        self._ballots = ballots
        self._election.set_ballots(ballots)

