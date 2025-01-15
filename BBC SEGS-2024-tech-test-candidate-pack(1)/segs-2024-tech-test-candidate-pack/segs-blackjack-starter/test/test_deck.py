import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        """Sets up the deck as well as the counts for test_rightCards()"""
        self.deck = Deck()
        self.aceCount = 0
        self.tenPictureCount = 0
        self.twoCount = 0
        self.threeCount = 0
        self.fourCount = 0
        self.fiveCount = 0
        self.sixCount = 0
        self.sevenCount = 0
        self.eightCount = 0
        self.nineCount = 0
        self.heartsCount = 0
        self.spadesCount = 0
        self.clubsCount = 0
        self.diamondsCount = 0

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):  # any method beginning with 'test_' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_rightCards(self):
        """Tests that there are 4 of each number/picture and 13 of each suit"""
        for i in self.deck.cards:
            if "Hearts" in i[0]:
                self.heartsCount += 1
            elif "Spades" in i[0]:
                self.spadesCount += 1
            elif "Clubs" in i[0]:
                self.clubsCount += 1
            elif "Diamonds" in i[0]:
                self.diamondsCount += 1
            else:
                raise Exception("Card does not belong to a suit")
            if isinstance(i[1], list):
                self.aceCount += 1
            elif i[1] == 10:
                self.tenPictureCount += 1
            elif i[1] == 2:
                self.twoCount += 1
            elif i[1] == 3:
                self.threeCount += 1
            elif i[1] == 4:
                self.fourCount += 1
            elif i[1] == 5:
                self.fiveCount += 1
            elif i[1] == 6:
                self.sixCount += 1
            elif i[1] == 7:
                self.sevenCount += 1
            elif i[1] == 8:
                self.eightCount += 1
            elif i[1] == 9:
                self.nineCount += 1
            else:
                raise Exception("Card does not have a valid score")
        self.assertEqual(self.heartsCount, 13)
        self.assertEqual(self.spadesCount, 13)
        self.assertEqual(self.clubsCount, 13)
        self.assertEqual(self.diamondsCount, 13)
        self.assertEqual(self.aceCount, 4)
        self.assertEqual(self.twoCount, 4)
        self.assertEqual(self.threeCount, 4)
        self.assertEqual(self.fourCount, 4)
        self.assertEqual(self.fiveCount, 4)
        self.assertEqual(self.sixCount, 4)
        self.assertEqual(self.sevenCount, 4)
        self.assertEqual(self.eightCount, 4)
        self.assertEqual(self.nineCount, 4)
        self.assertEqual(self.tenPictureCount, 16)



if __name__ == '__main__':
    unittest.main()
