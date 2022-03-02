import pygame
import random
from Game.fruitType import FruitType

class Fruit():
    def __init__(self, game):
        self.game = game
        self.image = pygame.transform.scale(pygame.image.load("img/limonka.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))

    def spawn(self):
        self.x = random.randint(0, self.game.gameBoard.width - 1)
        self.y = random.randint(0, self.game.gameBoard.height - 1)

        if self.game.gameBoard.fields[self.x][self.y].isFree:
            self.game.gameBoard.fields[self.x][self.y].fruitType = FruitType.common
        else:
            spawn()

    def draw(self):
        if self.game.isRun:
            self.game.screen.blit(self.image, self.game.gameBoard.fields[self.x][self.y].block)
