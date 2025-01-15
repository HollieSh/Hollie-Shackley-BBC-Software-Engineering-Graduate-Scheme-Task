import unittest
from src.hitorstand import HitOrStand
from src.deck import Deck


class HSTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_hit(self):  # any method beginning with 'test_' will be run by unittest
        """Tests that passing hit results in hit() being ran"""
        self.choice = "hit"
        self.playerOne = [["King of Spades", 10], ["2 of Spades", 2], ["2 of Hearts", 2]]
        self.playerScoreOne = 14
        self.dealerOne = [["Queen of Spades", 10], ["5 of Spades", 5]]
        self.playerTwo = [["5 of Spades", 5], ["9 of Spades", 9]]
        self.playerScoreTwo = 14
        self.dealerTwo = [["7 of Spades", 7], ["4 of Spades", 4]]
        self.playerThree = [["King of Spades",10], ["King of Hearts", 10]]
        self.playerScoreThree = 20
        self.dealerThree = [["Jack of Spades", 10], ["2 of Spades", 2]]
        self.caseOne = HitOrStand(self.deck.cards, self.playerOne, self.playerScoreOne, self.dealerOne, self.choice).run()
        self.caseTwo = HitOrStand(self.deck.cards, self.playerTwo, self.playerScoreTwo, self.dealerTwo, self.choice).run()
        self.caseThree = HitOrStand(self.deck.cards, self.playerThree, self.playerScoreThree, self.dealerThree, self.choice).run()
        #passing hit to this class results in an output of length 3, stand would result in None
        self.assertEqual(len(self.caseOne), 3)
        self.assertEqual(len(self.caseTwo), 3)
        self.assertEqual(len(self.caseThree), 3)

    def test_stand(self):
        """Tests that passing stand results in .stand() being run"""
        self.choice = "stand"
        self.playerOne = [["King of Spades", 10], ["2 of Spades", 2], ["2 of Hearts", 2]]
        self.playerScoreOne = 14
        self.dealerOne = [["Queen of Spades", 10], ["5 of Spades", 5]]
        self.playerTwo = [["5 of Spades", 5], ["9 of Spades", 9]]
        self.playerScoreTwo = 14
        self.dealerTwo = [["7 of Spades", 7], ["4 of Spades", 4]]
        self.playerThree = [["King of Spades",10], ["King of Hearts", 10]]
        self.playerScoreThree = 20
        self.dealerThree = [["Jack of Spades", 10], ["2 of Spades", 2]]
        self.caseOne = HitOrStand(self.deck.cards, self.playerOne, self.playerScoreOne, self.dealerOne, self.choice).run()
        self.caseTwo = HitOrStand(self.deck.cards, self.playerTwo, self.playerScoreTwo, self.dealerTwo, self.choice).run()
        self.caseThree = HitOrStand(self.deck.cards, self.playerThree, self.playerScoreThree, self.dealerThree, self.choice).run()
        #passing stand to this class results in an output of None, hit would give 3 values
        self.assertEqual(self.caseOne, None)
        self.assertEqual(self.caseTwo, None)
        self.assertEqual(self.caseThree, None)


if __name__ == '__main__':
    unittest.main()