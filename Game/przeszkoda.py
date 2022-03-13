import pygame
import random
from Game.przeszkodaType import PrzeszkodaType
from Game.przeszkodaDirection import PrzeszkodaDirection

class Przeszkoda():
    def __init__(self, game):
        self.game = game
        self.commonPrzeszkodaImage2 = pygame.transform.scale(pygame.image.load("img/cytryna.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.przeszkoda_list = [self.commonPrzeszkodaImage2]
        self.przeszkody = []

    def spawn(self):
        for przeszkodaDirection in self.przeszkody:
            while True:
                x = random.randint(0, self.game.gameBoard.width - 1)
                y = random.randint(0, self.game.gameBoard.height - 1)

                if self.game.gameBoard.fields[x][y].isFree and self.game.gameBoard.fields[x][y].przeszkodaType == PrzeszkodaType.none:
                    przeszkodaDirection.changePos(x, y)
                    self.game.gameBoard.fields[x][y].przeszkodaType = PrzeszkodaType.common
                    self.game.gameBoard.fields[x][y].przeszkodaDirection = przeszkodaDirection
                    break

    def respawn(self, przeszkodaDirection):
        self.game.gameBoard.fields[przeszkodaDirection.x][przeszkodaDirection.y].przeszkodaType = PrzeszkodaType.none
        if True:
            x = random.randint(0, self.game.gameBoard.width - 1)
            y = random.randint(0, self.game.gameBoard.height - 1)

            if self.game.gameBoard.fields[x][y].isFree and self.game.gameBoard.fields[x][y].przeszkodaType == PrzeszkodaType.none:
                przeszkodaDirection.changePos(x, y)
                self.game.gameBoard.fields[x][y].przeszkodaType = przeszkodaDirection.przeszkodaType
                self.game.gameBoard.fields[x][y].przeszkodaDirection = przeszkodaDirection

    def add(self, przeszkodaType):
        self.przeszkody.append(PrzeszkodaDirection(przeszkodaType))

    def draw(self):
        if self.game.isRun:
            for przeszkodaDirection in self.przeszkody:
                self.game.screen.blit(self.przeszkoda_list[0], self.game.gameBoard.fields[przeszkodaDirection.x][przeszkodaDirection.y].block)