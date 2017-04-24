from unittest import TestCase
from reachability import reach


class TestReachability(TestCase):
    def test_reachable(self):
        g = [
            [1],
            [0],
            [2],
            [3]
        ]
        self.assertTrue(reach(g, 0, 1), "Reachable")
        self.assertFalse(reach(g, 0, 2), "Unreachable")
