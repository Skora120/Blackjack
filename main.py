from blackjack.Deck import Deck
from blackjack.Player import Player
from blackjack.Croupier import Croupier


player = Player(200)
croupier = Croupier()
deck = Deck(3)

print(deck)
print(len(deck))
