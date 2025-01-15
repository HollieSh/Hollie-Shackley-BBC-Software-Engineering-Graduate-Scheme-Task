from src.deck import Deck
from src.deal import Deal
from src.opening import Opening
from src.score import Score
from src.finish import End
from src.hitorstand import HitOrStand


def play():
    cards = Deck().getCards()
    player, dealer = Opening(cards).setup()
    print ("\nYou have", player[0][0], "and", player[1][0])
    playerScore = Score(player).calculate()
    if playerScore == 21:
        #if a player gets blackjack, they win straight away
        print ("You Win")
        return
    print("The dealer's first card is", dealer[0][0])
    #both dealer cards are stored but only the first is revealed
    finishPlayer = False
    while finishPlayer == False:
        choice = input("Hit or stand?: ")
        if choice == "hit" or choice == "Hit" or choice == "HIT" or choice == "h" or choice == "H" or choice == "1":
            player, playerScore, bust = HitOrStand(cards, player, playerScore, dealer, "hit").run()
            if bust == True:
                #if the player has gone bust, exit the game
                return
        elif choice == "stand" or choice == "Stand" or choice == "STAND" or choice == "s" or choice == "S" or choice == "2":
            finishPlayer = True
            HitOrStand(cards, player, playerScore, dealer, "stand").run()
        else:
            print("please choice a valid choice")
            #continues to loop until the user enters a valid choice

if __name__ == '__main__':
    play()
