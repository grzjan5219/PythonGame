import pygame
import copy
from Game.field import Field

class Board():
    def __init__(self, width, height, game):
        self.width = width
        self.height = height
        self.game = game
        self.fields = [[None] * height] * width # dwuwymiarowa tablica pól planszy

        self.maxBoardSize = pygame.math.Vector2(940, 700)
        self.sizeBlock = int(min((self.maxBoardSize.x / width), (self.maxBoardSize.y / height)))
        self.boardSize = pygame.math.Vector2(self.sizeBlock * width, self.sizeBlock * height)

        margin = pygame.math.Vector2((self.maxBoardSize.x - self.boardSize.x) / 2, (self.maxBoardSize.y - self.boardSize.y) / 2)

        self.boardPos = pygame.math.Vector2(80, 80) + margin
        self.color1 = (150, 150, 150)
        self.color2 = (200, 200, 100)

        fieldPos = copy.deepcopy(self.boardPos)
        negationWidth = True
        negationHeight = True

        for x in range(width):
            fieldPos.y = self.boardPos.y
            self.fields[x] = [None] * height
            negationHeight = negationWidth
            negationWidth = not negationWidth
            for y in range(height):
                self.fields[x][y] = Field()
                self.fields[x][y].block = pygame.Rect(fieldPos.x, fieldPos.y, self.sizeBlock, self.sizeBlock)
                fieldPos.y += self.sizeBlock
                if negationHeight:
                    self.fields[x][y].color = self.color1
                    negationHeight = False
                else:
                    self.fields[x][y].color = self.color2
                    negationHeight = True
            fieldPos.x += self.sizeBlock

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(self.game.screen, self.fields[x][y].color, self.fields[x][y].block)

    def isExistField(self, pos):
        if (pos.x >= 0 and pos.x < self.width) and (pos.y >= 0 and pos.y < self.height):
            return True
        else:
            return False
