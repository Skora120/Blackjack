class Player:
    def __init__(self, amount=0):
        self.amount = amount
        self.hand = list()
        self.bet_amount = 0
        self.insurance = False
        self.is_surrender = False

    def add_card(self, card, deck):
        if card.value == 0:
            deck.shuffle()
            self.cards.insert(int(len(self.cards) * 0.25), card)
            self.hand.append(deck.cards.pop())
        else:
            self.hand.append(card)

    def clear_hand(self, deck):
        for card in self.hand:
            deck.cards.append(card)
        self.hand.clear()

    def total(self):
        total_value = 0
        aces_count = 0
        for card in self.hand:
            if card.value == 11:
                aces_count += 1
            total_value += card.value

        if total_value > 21 and aces_count > 0:
            while aces_count > 0:
                total_value -= 10
                if total_value < 21:
                    break
                aces_count -= 1

        return total_value

    def bet(self):
        while True:
            try:
                self.bet_amount = int(input("Bet amount (max:{}): ".format(self.amount)))
            except ValueError:
                print("Please enter value.")
                continue
            else:
                if self.amount - self.bet_amount < 0:
                    print("Please enter value.")
                    continue
                else:
                    self.amount -= self.bet_amount
                    break

    def hit(self, table):
        self.add_card(table.deck.cards.pop(), table.deck)
        table.draw()
        print('\'1\' Stand \n\'3\' Hit \n')
        while self.total() < 21:
            try:
                input_value = int(input(""))
            except ValueError:
                print("Please enter value.")
                continue
            else:
                if input_value not in [1, 3]:
                    continue

            if input_value == 1:
                   break
            else:
                table.draw()
                self.hit(table)

    def surrender(self):
        self.amount += int(self.bet_amount / 2)

    def double_down(self, table):
        self.add_card(table.deck.cards.pop(), table.deck)
        self.amount -= self.bet_amount
        self.bet_amount *= 2
        table.draw()

