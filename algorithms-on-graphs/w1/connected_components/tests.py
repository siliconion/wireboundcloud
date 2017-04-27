from unittest import TestCase
from connected_components import number_of_components


class TestReachability(TestCase):
    def test_reachable(self):
        g = [
            [1],
            [0],
            [3],
            [2]
        ]
        self.assertEqual(number_of_components(g), 2, "Two")
