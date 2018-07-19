class Deck:
    def __init__(self):
        self.cards = list()

    def remove_card(self, card):
        try:
            self.cards.remove(card)
        except ValueError:
            print("Card: {}, cannot be removed from deck".format(card))
