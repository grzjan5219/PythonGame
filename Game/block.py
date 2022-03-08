import pygame
import random
from pygame import mixer

class Food():
    def __init__(self, game):
        self.game = game
        self.commonFruitImage1 = pygame.transform.scale(pygame.image.load("img/limonka.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.commonFruitImage2 = pygame.transform.scale(pygame.image.load("img/cytryna.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.fruit_list = [self.commonFruitImage1, self.commonFruitImage2]
        self.fruits = []

    def spawn(self):
        for fruit in self.fruits:
            while True:
                x = random.randint(0, self.game.gameBoard.width - 1)
                y = random.randint(0, self.game.gameBoard.height - 1)

                if self.game.gameBoard.fields[x][y].isFree and self.game.gameBoard.fields[x][y].fruitType == FruitType.none:
                    fruit.changePos(x, y)
                    self.game.gameBoard.fields[x][y].fruitType = FruitType.common
                    self.game.gameBoard.fields[x][y].fruit = fruit
                    break

    def respawn(self, fruit):
        self.game.gameBoard.fields[fruit.x][fruit.y].fruitType = FruitType.none
        while True:
            x = random.randint(0, self.game.gameBoard.width - 1)
            y = random.randint(0, self.game.gameBoard.height - 1)

            if self.game.gameBoard.fields[x][y].isFree and self.game.gameBoard.fields[x][y].fruitType == FruitType.none:
                fruit.changePos(x, y)
                self.game.gameBoard.fields[x][y].fruitType = fruit.fruitType
                self.game.gameBoard.fields[x][y].fruit = fruit

    def add(self, fruitType):
        self.fruits.append(Fruit(fruitType))

    def draw(self):
        if self.game.isRun:
            for fruit in self.fruits:
                self.game.screen.blit(self.fruit_list[0], self.game.gameBoard.fields[fruit.x][fruit.y].block)