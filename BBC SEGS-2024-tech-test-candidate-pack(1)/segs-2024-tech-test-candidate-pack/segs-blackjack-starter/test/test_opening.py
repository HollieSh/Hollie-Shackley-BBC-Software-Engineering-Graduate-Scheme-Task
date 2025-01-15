import unittest
from src.opening import Opening
from src.deck import Deck


class OpenTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_openingNumber(self):  # any method beginning with 'test_' will be run by unittest
        self.hand1, self.hand2 = Opening(self.deck.cards).setup()
        #returns 2 hands - player and dealer
        self.assertEqual(len(self.hand1), 2)
        self.assertEqual(len(self.hand2), 2)

    def test_differentCards(self):
        """checks that the cards dealt are not equal to each other"""
        self.hand1, self.hand2 = Opening(self.deck.cards).setup()
        self.assertNotEqual(self.hand1[0], self.hand1[1])
        self.assertNotEqual(self.hand2[0], self.hand2[1])
        self.assertNotEqual(self.hand1[0], self.hand2[0])
        self.assertNotEqual(self.hand1[1], self.hand2[1])
        self.assertNotEqual(self.hand1[0], self.hand2[1])
        self.assertNotEqual(self.hand1[1], self.hand2[0])

if __name__ == '__main__':
    unittest.main()