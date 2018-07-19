class Card:
    def __init__(self, figure, colour, value):
        self.figure = figure
        self.colour = colour
        self.value = value

    def __str__(self):
        return "Figure: {}, Colour: {}, Value: {}".format(self.figure, self.colour, self.value)
