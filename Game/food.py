import pygame
import random
from Game.fruitType import FruitType
from Game.fruit import Fruit
from pygame import mixer
import copy
import math

class Food():
    def __init__(self, game):
        self.game = game
        self.counterLime = 0
        imageLime = pygame.image.load("img/limonka.png")
        self.commonFruitImage1 = pygame.transform.scale(imageLime, (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.commonFruitImage2 = pygame.transform.scale(pygame.image.load("img/cytryna.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.fruit_list = [self.commonFruitImage1, self.commonFruitImage2]
        #print(self.game.gameBoard.sizeBlock)

        self.ImagelimeList = []
        self.addedValue = 1
        # co który tick ma się wykonać tick()
        self.tickInvoke = 6
        self.currentTick = self.tickInvoke

        self.precision = 30 # więcej = płynniej = mniej wydajnie
        minScale = self.game.gameBoard.sizeBlock - (self.game.gameBoard.sizeBlock / 10.0) # 90%
        maxScale = self.game.gameBoard.sizeBlock + (self.game.gameBoard.sizeBlock / 2.0) # 150%

        precisionLime = (maxScale - minScale) / self.precision
        scaleLime = minScale

        for i in range(0, self.precision):
            val = (int(scaleLime) - self.game.gameBoard.sizeBlock) / 2
            self.ImagelimeList.append(pygame.transform.smoothscale(imageLime, (int(scaleLime), int(scaleLime))))
            scaleLime += precisionLime

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
                    fruit.rect = self.game.gameBoard.fields[x][y].block

                    for i in range(0, self.precision):
                        rect = self.ImagelimeList[i].get_rect()
                        rect.center = self.game.gameBoard.fields[fruit.x][fruit.y].block.center
                        fruit.animationPos[i] = pygame.math.Vector2(rect.x, rect.y)
                    break
        self.tick()

    def respawn(self, fruit):
        self.game.gameBoard.fields[fruit.x][fruit.y].fruitType = FruitType.none
        #self.game.gameBoard.fields[fruit.x][fruit.y].fruit = None
        while True:
            x = random.randint(0, self.game.gameBoard.width - 1)
            y = random.randint(0, self.game.gameBoard.height - 1)

            if self.game.gameBoard.fields[x][y].isFree and self.game.gameBoard.fields[x][y].fruitType == FruitType.none:
                fruit.changePos(x, y)
                self.game.gameBoard.fields[x][y].fruitType = fruit.fruitType
                self.game.gameBoard.fields[x][y].fruit = fruit

                fruit.rect = self.game.gameBoard.fields[x][y].block

                for i in range(0, self.precision):
                    rect = self.ImagelimeList[i].get_rect()
                    rect.center = self.game.gameBoard.fields[fruit.x][fruit.y].block.center
                    fruit.animationPos[i] = pygame.math.Vector2(rect.x, rect.y)

                # dźwięk jedzenia
                eat_sound = mixer.Sound("sounds/Eatting.mp3")
                eat_sound.set_volume(0.5)
                eat_sound.play()
                break

    def add(self, fruitType):
        newFruit = Fruit(fruitType)
        #newFruit.animationPos = copy.deepcopy(self.ImagelimeList)
        for i in range(0, self.precision):
            newFruit.animationPos.append(None)

        self.fruits.append(newFruit)

    def tick(self):

        if self.currentTick != self.tickInvoke:
            self.currentTick += 1
            return

        self.currentTick = 1

        for fruit in self.fruits:
            if fruit.fruitType == FruitType.common:
                self.counterLime += self.addedValue
                if self.counterLime == self.precision:
                    self.counterLime -= 1
                    self.addedValue = -1
                elif self.counterLime == 0:
                    self.addedValue = 1

    def draw(self):
        if self.game.isRun:
            for fruit in self.fruits:
                if fruit.fruitType == FruitType.common:
                    #rect = self.ImagelimeList[self.counterLime].get_rect()
                    #rect.center = self.game.gameBoard.fields[fruit.x][fruit.y].block.center
                    print(fruit.animationPos[self.counterLime])
                    self.game.screen.blit(self.ImagelimeList[self.counterLime], (fruit.animationPos[self.counterLime].x, fruit.animationPos[self.counterLime].y))
