from Game.fruitType import FruitType

class Fruit():
    def __init__(self, fruitType):
        self.rect = None
        self.fruitType = fruitType
        self.animationPos = []
        self.x = 0
        self.y = 0

    def changePos(self, x, y):
        self.x = x
        self.y = y