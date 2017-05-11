from unittest import TestCase
from acyclicity import acyclic


class TestAcyclicity(TestCase):
    def test_reachable(self):
        g = [[1],
             [2],
             [0],
             [0]]
        self.assertEqual(acyclic(g), 0, "Not Acylic")
        g = [[1, 2, 3],
             [2, 4],
             [3, 4],
             [],
             []]
        self.assertEqual(acyclic(g), 1, "Acylic")
