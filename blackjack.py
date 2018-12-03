from card import Card
from player import Player

class BlackJack:
    WELCOME_MSG = '''
Welcome to BlackJack! Type the following input to interact with the game:
'h' = hit, or take another card
's' = stand, or stop taking cards
'q' = quit, or stop playing
Just don't go over 21!
'''

    @staticmethod
    def play():
        '''
        Play a simple interactive version of BlackJack between 2 players
        '''
        print(BlackJack.WELCOME_MSG)
        deck = Card.populateDeck()

        player = Player(deck.pop(), "Player")
        dealer = Player(deck.pop(), "Dealer")

        done = False
        prevInput = None
        currPlayer, nextPlayer = player, dealer

        # Keep looping until a player passes 21, both stand, or a user enters 'q'
        while not done:
            s = input(f"{currPlayer}, make your move.\n")
            invalidInput = False
            if s is "s": # Stand
                print(f'{currPlayer} stands. Your value is still {currPlayer.value}.')
                if prevInput is "s":
                    # If both players stand, determine winner
                    if currPlayer.value > nextPlayer.value:
                        print(f"{currPlayer} wins!")
                    elif currPlayer.value < nextPlayer.value:
                        print(f"{nextPlayer} wins!")
                    else:
                        print("It's a tie!")
                    done = True
            elif s is "h": # Hit
                done = currPlayer.dealCard(deck.pop())
                if done:
                    print(f'{nextPlayer} wins!')
            elif s is "q": # Quit
                print("Thanks for playing!")
                done = True
            else:
                invalidInput = True
                print("Invalid input. Please enter 's' to stand, 'h' to hit, or 'q' to quit.")

            if not done and not invalidInput:
                # Switch players and record prev input
                currPlayer, nextPlayer = nextPlayer, currPlayer
                prevInput = s


if __name__ == '__main__':
    BlackJack.play()
