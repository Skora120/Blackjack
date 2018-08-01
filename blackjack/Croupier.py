from .Player import Player


class Croupier(Player):
    def __init__(self):
        super().__init__()

    def hit(self, table):
        while self.total() < 21:
            if self.total() == 17:
                aces_count = 0
                for card in self.hand:
                    if card.value == 11:
                        aces_count += 1
                if aces_count > 0:
                    self.add_card(table.deck.cards.pop(), table.deck)
                    table.draw()
                else:
                    break

            elif self.total() < 17:
                self.add_card(table.deck.cards.pop(), table.deck)
                table.draw()

            else:
                break
