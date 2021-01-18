from unittest import TestCase
from bipartite import bipartite


class TestToposort(TestCase):
    def test_distance(self):
        g = [
            [1, 2, 3],
            [0, 2],
            [0, 1],
            [0]
        ]
        self.assertEqual(bipartite(g), False, bipartite(g))
        g = [
            [1, 2],
            [0, 2],
            [0, 1],
            [4],
            [3]
        ]
        self.assertEqual(bipartite(g), True, "no path")
