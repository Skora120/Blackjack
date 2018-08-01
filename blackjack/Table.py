from .Deck import Deck
from .Player import Player
from .Croupier import Croupier
from .Card import Card
import os


class Table:
    def __init__(self, amount=1500, decl_multiplier=4):
        self.deck = Deck(decl_multiplier)
        self.player = Player(amount)
        self.player_split = None
        self.croupier = Croupier()

        self.is_player_stand = False
        self.is_player_split_stand = False

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw(self):
        self.clear_screen()

        if self.is_player_stand:
            print('Croupier Cards:')
            for card in self.croupier.hand:
                print(card)
            print('Total: {} \n'.format(self.croupier.total()))
            print('Player Cards:')
            for card in self.player.hand:
                print(card)
            print('Total: {} \n'.format(self.player.total()))

            if self.player_split is not None:
                print('Player hand 2 Cards:')
                for card in self.player_split.hand:
                    print(card)
                print('Total: {} \n'.format(self.player_split.total()))
        else:
            print('Croupier Cards:')
            print(self.croupier.hand[0])
            print(Card('?', '?', '?', 0))
            print('Total: {} \n'.format(self.croupier.hand[0].value))
            print('Player Cards: ')
            for card in self.player.hand:
                print(card)
            print('Total: {} \n'.format(self.player.total()))

            if self.player_split is not None:
                print('Player hand 2 Cards:')
                for card in self.player_split.hand:
                    print(card)
                print('Total: {} \n'.format(self.player_split.total()))

    def give_cards_at_start(self):
        self.player.add_card(self.deck.cards.pop(), self.deck)
        self.croupier.add_card(self.deck.cards.pop(), self.deck)

        self.player.add_card(self.deck.cards.pop(), self.deck)
        self.croupier.add_card(self.deck.cards.pop(), self.deck)

    def check_win(self, player):
        if player.insurance and self.croupier.total() == 21:
            print('Player won insurance')
            player.amount += player.bet_amount * 2
            player.insurance = False

        if not player.is_surrender:
            if player.total() == self.croupier.total() and player.total() <= 21:
                player.amount += player.bet_amount
                player.bet_amount = 0
                print('Push - bets returned')

            elif player.total() > 21:
                print('Player lost: {}'.format(player.bet_amount))
                player.bet_amount = 0

            elif self.croupier.total() > 21 or self.croupier.total() < self.player.total():
                winning = 0
                if player.total() == 21 and 11 in [player.hand[0].value, player.hand[1].value] and \
                        10 in [player.hand[0].value, player.hand[1].value]:
                    winning = int(player.bet_amount * 2.5)
                    player.amount += winning
                    player.bet_amount = 0
                    print('Player got BlackJack!')

                elif player.total() <= 21:
                    winning = player.bet_amount
                    player.amount += winning * 2
                    player.bet_amount = 0

                print('Player won: {}'.format(winning))
            elif self.croupier.total() > player.total():
                print('Player lost: {}'.format(player.bet_amount))
                player.bet_amount = 0

            else:
                print('Player won: '.format(player.bet_amount))
                player.amount += player.bet_amount
                player.bet_amount = 0
        else:
            player.is_surrender = False

        player.clear_hand(self.deck)

    def split(self):
        self.player_split = Player()
        self.player.bet_amount /= 2
        self.player_split.bet_amount = self.player.bet_amount
        self.player_split.hand.append(self.player.hand.pop())

        print("Player first hand:  \n")
        self.player.hit(self)
        print("Player second hand:  \n")
        self.player_split.hit(self)
        self.is_player_stand = True

    def reset_round(self):
        self.croupier.clear_hand(self.deck)
        self.is_player_stand = False
        self.player_split = None
        self.is_player_split_stand = False

    def play_round(self):
        while self.player.amount > 0:
            self.player.bet()
            self.give_cards_at_start()
            is_split_available = False
            is_insurance_available = False

            while self.player.total() < 21:
                self.draw()
                menu = 'What you want to do : \n' \
                       '\'1\' Stand \n' \
                       '\'2\' Double Down \n' \
                       '\'3\' Hit \n' \
                       '\'4\' Surrender \n'

                if self.croupier.hand[0].face == 'Ace' and not self.player.insurance:
                    menu += '\'5\' Insurance \n'
                    is_insurance_available = True

                if self.player.hand[0].face == self.player.hand[1].face:
                    menu += '\'6\' Split \n'
                    is_split_available = True

                try:
                    choose = int(input(menu))
                except ValueError:
                    print("Please enter value.")
                    continue
                else:
                    if choose not in range(1, 7):
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
                            self.player.is_surrender = True
                            break
                        elif choose == 5 and is_insurance_available:
                            self.player.amount -= int(self.player.bet_amount / 2)
                            self.player.insurance = True
                            continue
                        elif choose == 6 and is_split_available:
                            self.split()
                            break
                        else:
                            print("ERROR")

            self.is_player_stand = True
            self.croupier.hit(self)
            self.draw()

            if self.player_split:
                print("Second hand: ")
                self.check_win(self.player_split)
                self.player.amount += self.player_split.amount

            print('\n')
            self.check_win(self.player)

            self.reset_round()
