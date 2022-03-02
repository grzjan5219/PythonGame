import pygame
import random
from Game.fruitType import FruitType
from Game.fruit import Fruit

class Food():
    def __init__(self, game):
        self.game = game
        self.commonFruitImage = pygame.transform.scale(pygame.image.load("img/limonka.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.fruits = []

    def spawn(self):
        for fruit in self.fruits:
            while True:
                x = random.randint(0, self.game.gameBoard.width - 1)
                y = random.randint(0, self.game.gameBoard.height - 1)

                if self.game.gameBoard.fields[x][y].isFree:
                    fruit.changePos(x, y)
                    self.game.gameBoard.fields[x][y].fruitType = FruitType.common
                    self.game.gameBoard.fields[x][y].fruit = fruit
                    break

    def respawn(self, fruit):
        self.game.gameBoard.fields[fruit.x][fruit.y].fruitType = FruitType.none
        #self.game.gameBoard.fields[fruit.x][fruit.y].fruit = None
        while True:
            x = random.randint(0, self.game.gameBoard.width - 1)
            y = random.randint(0, self.game.gameBoard.height - 1)

            if self.game.gameBoard.fields[x][y].isFree:
                fruit.changePos(x, y)
                self.game.gameBoard.fields[x][y].fruitType = FruitType.common
                self.game.gameBoard.fields[x][y].fruit = fruit
                break

    def add(self, fruitType):
        self.fruits.append(Fruit(fruitType))

    def draw(self):
        if self.game.isRun:
            for fruit in self.fruits:
                self.game.screen.blit(self.commonFruitImage, self.game.gameBoard.fields[fruit.x][fruit.y].block)
