class Deck:

    def __init__(self):
        self.cards = []
        self.suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
        for i in range (1,14):
            #for each number/picture
            if i == 12 or i == 13 or i==11:
                #if a picture card
                self.thisScore = 10
            elif i != 1:
                self.thisScore = i
            else:
                #if an ace
                self.thisScore = [1, 11]
            for x in self.suits:
                #for each suit
                if i == 1:
                    self.thisName = "Ace of " + x
                elif i == 11:
                    self.thisName = "Jack of " + x
                elif i == 12:
                    self.thisName = "Queen of " + x
                elif i == 13:
                    self.thisName = "King of " + x
                else:
                    self.thisName = str(i) + " of " + x
                self.thisCard = [self.thisName, self.thisScore]
                #cards are scored as the display of the card followed by its value in the game
                self.cards.append(self.thisCard)
    
    def getCards(self):
        """Getter for the deck of cards"""
        return self.cards
