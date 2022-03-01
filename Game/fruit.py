import pygame
import random
from Game.fruitType import FruitType

class Fruit():
    def __init__(self, game):
        self.game = game
        #self.image = pygame.image.load("img/limonka.png")

    def spawn(self):
        x = random.randint(0, self.game.gameBoard.width - 1)
        y = random.randint(0, self.game.gameBoard.height - 1)

        if self.game.gameBoard.fields[x][y].isFree:
            self.game.gameBoard.fields[x][y].fruitType = FruitType.common
            self.game.gameBoard.fields[x][y].color = (0, 0, 0)
        else:
            spawn()