from src.deal import Deal

class Opening:

    def __init__(self, cards):
        self.cards = cards
        self.player = []
        self.dealer = []
        self.deal = Deal(cards)

    def setup(self):
        """Deals opening hands to the dealer and player"""
        one = self.deal.giveCard()
        two = self.deal.giveCard()
        three = self.deal.giveCard()
        four = self.deal.giveCard()
        self.player.append(one)
        self.player.append(three)
        self.dealer.append(two)
        self.dealer.append(four)
        #deals to player, dealer, player then dealer
        return self.player, self.dealer