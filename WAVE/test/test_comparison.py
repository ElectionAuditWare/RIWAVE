import random
import unittest
from audit import Comparison
import data_gen
from election import Ballot

class TestAudit(unittest.TestCase):
    def setup_comparison(self):
        cp = Comparison()
        return cp


    def test_comparison_pres_2016(self):
        random.seed(0)
        ballot_count = 100
        pres = data_gen.Pres2016()
        pres.gen_ballots(ballot_count, 0.05)
        e = pres.get_election()

        rla = self.setup_comparison()
        rla.init(pres.get_reported_results(), e.get_ballot_count())
        rla.set_parameters([5, 1.03905,0.001,0.0001,0.001,0.0001])
        rla.recompute(e.get_ballots(), pres.get_reported_results())
        self.assertEqual(rla._stopping_count, 96)

        # Change actual value for ballots
        changed_contestant = e.get_contestants()[0]
        election_ballots = e.get_ballots()
        initial_ballots = election_ballots.copy()
        for i in range(5):
            election_ballots[i].set_actual_value(changed_contestant)

        rla.recompute(election_ballots, pres.get_reported_results())
        self.assertEqual(rla._stopping_count, 87)