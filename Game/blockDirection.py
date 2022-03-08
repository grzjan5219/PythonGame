from Game.blockType import BlockType

class BlockDirection():
    def __init__(self, fruitType):
        self.fruitType = fruitType
        self.x = 0
        self.y = 0

    def changePos(self, x, y):
        self.x = x
        self.y = y