import random

class Deal:

    def __init__(self, cards):
        self.done = []
        #keep track in order to not deal the same card twice
        self.cards = cards
        
    def giveCard(self):
        self.which = random.randint(0,51)
        #picks a number which corresponds to a card
        while self.which in self.done:
            self.which = random.randint(0,51)
        self.dealt = self.cards[self.which]
        #gets the card
        self.done.append(self.which)
        return self.dealt