import unittest
from src.score import Score


class ScoreTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        #self.deck = Deck()
        pass

    def tearDown(self):  # this method will be run after each test
        pass

    def test_getsTwentyOne(self):  # any method beginning with 'test_' will be run by unittest
        """Tests the given scenarios that result in a score of 21"""
        self.caseOne = Score([['9 of Spades', 9],['Ace of Spades', [1,11]],['Ace of Hearts', [1,11]]]).calculate()
        self.assertEqual(self.caseOne, 21)
        self.caseTwo = Score([['King of Spades', 10],['Queen of Spades', 10], ['Ace of Spades', [1,11]]]).calculate()
        self.assertEqual(self.caseTwo, 21)
        self.caseThree = Score([['King of Spades', 10],['Ace of Spades', [1,11]]]).calculate()
        self.assertEqual(self.caseThree, 21)

    def test_bustHand(self):
        """Tests 3 hands which give a bust hand"""
        self.caseOne = Score([["King of Spades", 10],["2 of Spades", 2],["King of Hearts", 10]]).calculate()
        self.assertEqual(self.caseOne, "bust")
        self.caseTwo = Score([["King of Spades", 10],["7 of Spades", 7],["Queen of Spades", 10]]).calculate()
        self.assertEqual(self.caseTwo, "bust")
        self.caseThree = Score([["Ace of Spades", [1,11]],["8 of Spades", 8],["King of Spades", 10],["King of Hearts", 10]]).calculate()
        self.assertEqual(self.caseThree, "bust")

    def test_validHand(self):
        """Tests 3 hands which give a valid hand and score"""
        self.caseOne = Score([["7 of Spades", 7],["8 of Spades", 8],["5 of Spades", 5]]).calculate()
        self.assertEqual(self.caseOne, 20)
        self.caseTwo = Score([["3 of Spades", 3],["4 of Spades", 4]]).calculate()
        self.assertEqual(self.caseTwo, 7)
        self.caseThree = Score([["10 of Spades", 10],["2 of Spades", 2],["Ace of Spaces", [1,11]]]).calculate()
        self.assertEqual(self.caseThree, 13)


if __name__ == '__main__':
    unittest.main()
