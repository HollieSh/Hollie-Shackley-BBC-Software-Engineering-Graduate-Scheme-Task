from src.score import Score
from src.deal import Deal

class End:

    def __init__(self, player, playerScore, dealer, cards):
        self.player = player
        self.playerScore = playerScore
        self.dealer = dealer
        self.cards = cards

    def finish(self):
        """Completes the dealer's game"""
        self.dealerScore = Score(self.dealer).calculate()
        print("\nThe second dealer card is", self.dealer[1][0])
        #the dealer's second card is turned over
        if self.dealerScore == 21:
            print("\nThe dealer wins")
            #if player gets blackjack, already declared so if dealer gets here, must have won
            return False
            #the game ends once a winner is declared
        self.finish = False
        while self.finish == False:
            if self.dealerScore >= 17:
                self.finish = True
                #the dealer stands on 17 or over
            else:
                #the dealer must hit under 17
                another = Deal(self.cards).giveCard()
                self.dealer.append(another)
                self.dealerScore = Score(self.dealer).calculate()
                print("The dealer's next card is", another[0])
                if self.dealerScore == "bust":
                    print("\nThe dealer has exceeded 21, you win")
                    return False
        return True
        #informs blackjack.py to continue as no player has got blackjack or gone bust

    def whoWins(self):
        """As no one has got blackjack or gone bust, calculates the highest score"""
        if self.playerScore > self.dealerScore:
            print("\nYou win")
        elif self.playerScore == self.dealerScore:
            print("\nYou and the dealer draw")
        else:
            print("\nDealer wins")