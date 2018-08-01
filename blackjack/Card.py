class Card:
    def __init__(self, figure, colour, face, value):
        self.figure = figure
        self.colour = colour
        self.value = value
        self.face = face

    def __str__(self):
        return "Figure: {}, Colour: {}, Face: {}, Value: {}".format(self.figure, self.colour, self.face, self.value)
