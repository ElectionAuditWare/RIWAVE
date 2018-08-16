import random
import unittest
from audit import BallotPolling
import data_gen
from election import Ballot

class TestAudit(unittest.TestCase):
    def setup_ballot_polling(self):
        bp = BallotPolling()
        return bp

    def test_get_progress(self):
        bp = self.setup_ballot_polling()
        self.assertEqual("T = 1.0000",bp.get_progress())

    def test_get_status(self):
        bp = self.setup_ballot_polling()
        self.assertEqual("In Progress",bp.get_status())
        bp._status = 1
        self.assertEqual("Election Results Verified",bp.get_status())
        bp._status = 2
        self.assertEqual("Full Hand Count Required",bp.get_status())

    def test_get_name(self):
        bp = self.setup_ballot_polling()
        self.assertEqual("Ballot Polling Audit",bp.get_name())

    def test_get_params(self):
        bp = self.setup_ballot_polling()
        bp._tolerance = 0.01
        self.assertEqual([['Tolerance', '1.00%']],bp.get_parameters())

    def test_set_parameters(self):
        bp = self.setup_ballot_polling()
        bp.set_parameters([1,])
        self.assertEqual(bp._tolerance,0.01)

    def test_ballot_polling_pres_2016(self):
        random.seed(0)
        ballot_count = 100
        pres = data_gen.Pres2016()
        pres.gen_ballots(ballot_count, 0.05)
        e = pres.get_election()

        rla = self.setup_ballot_polling()
        rla.init(pres.get_reported_results(), e.get_ballot_count())
        rla.set_parameters([1])
        rla.recompute(e.get_ballots(), pres.get_reported_results())
        self.assertEqual(rla.get_progress(),'T = 1.0464')
        # Change actual value for ballots
        changed_contestant = e.get_contestants()[0]
        election_ballots = e.get_ballots()
        initial_ballots = election_ballots.copy()
        for i in range(5):
            election_ballots[i].set_actual_value(changed_contestant)
        print("Different ballots: %d" % sum([(election_ballots[i]._actual_value._id != initial_ballots[i]._actual_value._id) for i in range(len(election_ballots))]) )

        rla.recompute(election_ballots, pres.get_reported_results())
        self.assertEqual(rla.get_progress(),'T = 1.1990')