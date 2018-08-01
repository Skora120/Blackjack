from blackjack.Deck import Deck
from blackjack.Player import Player
from blackjack.Croupier import Croupier
from blackjack.Table import Table
import os


player = Player(200)
croupier = Croupier()
deck = Deck(1)

# print(deck)
# print(len(deck))

# Logic alpha version /// 1P

# TEST

crop = Croupier()
print(crop.hand)
# /TEST


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


table = Table()
table.play_round()


















while False:
    player.bet()

    player.clear_hand(deck)
    croupier.clear_hand(deck)

    player.add_card(deck.cards.pop())
    croupier.add_card((deck.cards.pop()))

    player.add_card(deck.cards.pop())
    croupier.add_card((deck.cards.pop()))

    for card in player.hand:
        print(card, '\n')

    while player.total() < 21:
        choose = 0

        print("Croupier: ", croupier.hand[0])
        print("Player: ", player.hand[0], player.hand[1], "Total: {}".format(player.total()))

        try:
            choose = int(input('What you want to do : \n'
                               '\'1\' Stand \n'
                               '\'2\' Double Down \n'
                               '\'3\' Hit \n'
                               '\'4\' Surrender \n'
                               '\'5\' Split \n'))
        except ValueError:
            print("Please enter value.")
            continue
        else:
            if choose not in range(1, 5):
                continue
            else:
                if choose == 1:
                    break
                elif choose == 2:
                    player.double_down(deck)
                    break
                elif choose == 3:
                    player.hit(deck)
                    break
                elif choose == 4:
                    player.surrender()
                    break
                elif choose == 5:
                    break
                else:
                    print("ERROR")


