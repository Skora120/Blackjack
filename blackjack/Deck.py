from .Card import Card
from random import shuffle


class Deck:
    def __init__(self, multiplier=1):
        self.cards = list()
        self.multiplier = multiplier

        for i in range(0, self.multiplier):
            for j in range(0, 4):
                for k in range(2, 11):
                    if j == 0:
                        self.cards.append(Card('Clubs', 'Black', k, k))
                    elif j == 1:
                        self.cards.append(Card('Diamonds', 'Red', k, k))
                    elif j == 2:
                        self.cards.append(Card('Hearts', 'Red', k, k))
                    else:
                        self.cards.append(Card('Spades', 'Black', k, k))

                if j == 0:
                    self.cards.append(Card('Clubs', 'Black', 'Ace', 11))
                    self.cards.append(Card('Clubs', 'Black', 'King', 10))
                    self.cards.append(Card('Clubs', 'Black', 'Queen', 10))
                    self.cards.append(Card('Clubs', 'Black', 'Jack', 10))
                elif j == 1:
                    self.cards.append(Card('Diamonds', 'Red', 'Ace', 11))
                    self.cards.append(Card('Diamonds', 'Red', 'King', 10))
                    self.cards.append(Card('Diamonds', 'Red', 'Queen', 10))
                    self.cards.append(Card('Diamonds', 'Red', 'Jack', 10))
                elif j == 2:
                    self.cards.append(Card('Hearts', 'Red', 'Ace', 11))
                    self.cards.append(Card('Hearts', 'Red', 'King', 10))
                    self.cards.append(Card('Hearts', 'Red', 'Queen', 10))
                    self.cards.append(Card('Hearts', 'Red', 'Jack', 10))
                else:
                    self.cards.append(Card('Spades', 'Black', 'Ace', 11))
                    self.cards.append(Card('Spades', 'Black', 'King', 10))
                    self.cards.append(Card('Spades', 'Black', 'Queen', 10))
                    self.cards.append(Card('Spades', 'Black', 'Jack', 10))

        shuffle(self.cards)

        self.cards.insert(int(len(self.cards) * 0.25), Card('Red Card', 'None', 'None', 0))

    def __str__(self):
        return '\n'.join(str(p) for p in self.cards)

    def __len__(self):
        return len(self.cards)

