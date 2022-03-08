from Game.przeszkodaType import PrzeszkodaType

class PrzeszkodaDirection():
    def __init__(self, przeszkodaType):
        self.przeszkodaType = przeszkodaType
        self.x = 0
        self.y = 0

    def changePos(self, x, y):
        self.x = x
        self.y = y