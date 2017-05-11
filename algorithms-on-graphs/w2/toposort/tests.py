from unittest import TestCase
from toposort import toposort


class TestToposort(TestCase):
    def test_toposort(self):
        g = [
            [],
            [0],
            [1],
            [2]
        ]
        self.assertEqual(toposort(g), [3, 2, 0, 1], "Link list")
        g = [
            [1],
            [2],
            [3],
            []
        ]
        self.assertEqual(toposort(g), [0, 1, 2, 3], "Link list")
        g = [
            [1],
            [],
            [],
            []
        ]
        self.assertEqual(toposort(g), [3, 2, 0, 1], "Link list")

