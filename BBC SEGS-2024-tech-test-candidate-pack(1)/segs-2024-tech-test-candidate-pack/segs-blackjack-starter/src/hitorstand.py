from src.deal import Deal
from src.score import Score
from src.finish import End

class HitOrStand:

    def __init__(self, cards, player, playerScore, dealer, choice):
        self.cards = cards
        self.player = player
        self.choice = choice
        self.playerScore = playerScore
        self.dealer = dealer

    def hit(self):
        self.another = Deal(self.cards).giveCard()
        self.player.append(self.another)
        self.playerScore = Score(self.player).calculate()
        #gives the player another card and updates the score
        print("Your next card is", self.another[0])
        if self.playerScore == "bust":
            print("\nYou have exceeded 21, you lose")
            #bust hands are revealed immediately
            return self.player, self.playerScore, True
            #flag is set to False to show that play should not continue
        return self.player, self.playerScore, False
    
    def stand(self):
        self.process = End(self.player, self.playerScore, self.dealer, self.cards)
        self.result = self.process.finish()
        #call to the function which processes the dealer actions at the end of a game
        if self.result == True:
            self.process.whoWins()
            #as long as no-one has blackjack or has gone bust, calculates the higher score
        return
    
    def run(self):
        """Directs the call based on the input to hit or stand"""
        if self.choice == "hit":
            return(self.hit())
        else:
            self.stand()