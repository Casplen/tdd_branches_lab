import unittest

from src.high_scores import latest, personal_best, personal_top_three, sort_highest_to_lowest

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.scores1 = [10, 44, 23, 48, 8]
        self.scores2 = [22, 32, 32, 12, 9]
        self.scores3 = [12, 26]
        self.scores4 = [50]
    # Tests

    

    # Test latest score (the last thing in the list)

    def test_latest_score(self):
        self.assertEqual(8, latest(self.scores1))

    # Test personal best (the highest score in the list)

    def test_highest_score(self):
        self.assertEqual(48, personal_best(self.scores1))

    # Test top three from list of scores
    def test_top_three_scores(self):
        top_three = [48, 44 ,23]
        self.assertEqual(top_three, personal_top_three(self.scores1))

    # Test ordered from highest tp lowest
    def test_ordered_highest_to_lowest(self):
        highest_to_lowest = [48, 44, 23, 10, 8]
        self.assertEqual(highest_to_lowest, sort_highest_to_lowest(self.scores1))

    # Test top three when there is a tie

    def test_top_three_when_tied(self):
        top_three = [32, 32, 22]
        self.assertEqual(top_three, personal_top_three(self.scores2))

    # Test top three when there are less than three

    def test_top_three_when_less_than_three_scores(self):
        top_three = [26, 12]
        self.assertEqual(top_three, personal_top_three(self.scores3))
        

    # Test top three when there is only one
    def test_top_three_when_only_one_score(self):
        top_three = [50]
        self.assertEqual(top_three, personal_top_three(self.scores4))

