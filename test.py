import unittest
from Knuth import KnuthMorris


class TestSolution(unittest.TestCase):

    def test_1(self):
        text = "mmmmmmmmmmmmmmmm"
        pattern = "m"
        self.assertEqual(KnuthMorris(text, pattern).Knuth_Morris_Pratt_algorithm(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ])

    def test_2(self):
        text = "maksmaksmaksmaksmaksmaksmaks"
        pattern = "maksmaks"
        self.assertEqual(KnuthMorris(text, pattern).Knuth_Morris_Pratt_algorithm(), [0, 4, 8, 12, 16, 20])

    def test_3(self):
        text = "maksdemmaksmdemaksmaksdemmaksdmakdamke"
        pattern = "maksdem"
        self.assertEqual(KnuthMorris(text, pattern).Knuth_Morris_Pratt_algorithm(), [0, 18])