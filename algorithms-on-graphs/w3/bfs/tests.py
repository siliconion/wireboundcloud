from unittest import TestCase
from bfs import distance


class TestToposort(TestCase):
    def test_distance(self):
        g = [
            [1, 2, 3],
            [0, 2],
            [0, 1],
            [0]
        ]
        self.assertEqual(distance(g, 1, 3), 2, distance(g, 1, 3))
        g = [
            [1, 2],
            [0, 2],
            [0, 1],
            [4],
            [3]
        ]
        self.assertEqual(distance(g, 0, 4), -1, "no path")
