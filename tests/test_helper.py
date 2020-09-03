import unittest
from minesweeper_model import helper


class TestHelper(unittest.TestCase):
    def test_surrounding_tiles(self):
        actual = helper.surrounding_tiles(4, 2)
        expected = [(3, 3), (4, 3), (5, 3),
                    (3, 2), (5, 2),
                    (3, 1), (4, 1), (5, 1)]
        self.assertCountEqual(actual, expected)

        actual = helper.surrounding_tiles(0, 1, True)
        expected = [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]
        self.assertCountEqual(actual, expected)
