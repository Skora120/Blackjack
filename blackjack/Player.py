class Player:
    def __init__(self, amount=0):
        self.amount = amount
        self.hand = list()

    def add_card(self, card):
        self.hand += card

    def clear_hand(self):
        self.hand.clear()

