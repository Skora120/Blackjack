from .Deck import Deck
from .Player import Player
from .Croupier import Croupier
from .Card import Card


class Table:
    def __init__(self):
        self.deck = Deck(4)
        self.player = Player(1500)
        self.croupier = Croupier()

        self.is_player_stand = False

    def draw(self):
        if self.is_player_stand:
            print('Croupier Cards:')
            for card in self.croupier.hand:
                print(card)
            print('Total: {} \n'.format(self.croupier.total()))
            print('Player Cards:')
            for card in self.player.hand:
                print(card)
            print('Total: {} \n'.format(self.player.total()))
        else:
            print('Croupier Cards:')
            print(self.croupier.hand[0])
            print(Card('?', '?', '?', 0))
            print('Total: {} \n'.format(self.croupier.hand[0].value))
            print('Player Cards: ')
            for card in self.player.hand:
                print(card)
            print('Total: {} \n'.format(self.player.total()))

    def give_cards_at_start(self):
        self.player.add_card(self.deck.cards.pop(), self.deck)
        self.croupier.add_card(self.deck.cards.pop(), self.deck)

        self.player.add_card(self.deck.cards.pop(), self.deck)
        self.croupier.add_card(self.deck.cards.pop(), self.deck)

    def check_win(self):
        if self.player.insurance == True and self.croupier.total() == 21:
            print('Player won insurance')
            self.player.amount += self.player.bet_amount * 2
            self.player.insurance = False

        if self.player.total() == self.croupier.total() and self.player.total() < 21:
            self.player.amount += self.player.bet_amount
            self.player.bet_amount = 0
            print('Push - bets returned')

        elif self.player.total() > 21:
            print('Player lost: {}'.format(self.player.bet_amount))
            self.player.bet_amount = 0

        elif self.croupier.total() > 21:
            winning = 0
            if self.player.total() == 21 and 11 in self.player.hand and 10 in self.player.hand:
                winning = int(self.player.bet_amount * 2.5)
                self.player.amount += winning
                self.player.bet_amount = 0

            elif self.player.total() <= 21:
                winning = self.player.bet_amount
                self.player.amount += winning * 2
                self.player.bet_amount = 0

            print('Player won: {}'.format(winning))
        elif self.croupier.total() > self.player.total():
            print('Player lost: {}'.format(self.player.bet_amount))
            self.player.bet_amount = 0

        else:
            print('Player won: '.format(self.player.bet_amount))
            self.player.amount += self.player.bet_amount
            self.player.bet_amount = 0

        self.player.clear_hand(self.deck)
        self.croupier.clear_hand(self.deck)

    def play_round(self):
        while self.player.amount > 0:
            self.player.bet()
            self.give_cards_at_start()

            while self.player.total() < 21:
                self.draw()
                options = 5
                menu = 'What you want to do : \n' \
                       '\'1\' Stand \n' \
                       '\'2\' Double Down \n' \
                       '\'3\' Hit \n' \
                       '\'4\' Surrender \n'
                # TODO Split

                if self.croupier.hand[0].face == 'Ace':
                    menu += '\'{}\' Insurance \n'.format(options)
                    options += 1
                    self.player.amount -= int(self.player.bet_amount / 2)
                    self.player.insurance = True

                try:
                    choose = int(input(menu))
                except ValueError:
                    print("Please enter value.")
                    continue
                else:
                    if choose not in range(1, options):
                        continue
                    else:
                        if choose == 1:
                            break
                        elif choose == 2:
                            self.player.double_down(self)
                            break
                        elif choose == 3:
                            self.player.hit(self)
                            break
                        elif choose == 4:
                            self.player.surrender()
                            break
                        elif choose == 5:
                            break
                        elif choose == 6:
                            break
                        else:
                            print("ERROR")
            self.is_player_stand = True
            self.croupier.hit(self)
            self.draw()
            self.check_win()
            self.is_player_stand = False
