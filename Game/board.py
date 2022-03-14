import pygame
import copy
from Game.field import Field

class Board():
    def __init__(self, width, height, game):
        self.width = width
        self.height = height
        self.game = game
        self.fields = [[None] * height] * width
        self.maxBoardSize = pygame.math.Vector2(1200, 880)
        self.sizeBlock = int(min((self.maxBoardSize.x / width), (self.maxBoardSize.y / height)))
        self.boardSize = pygame.math.Vector2(self.sizeBlock * width, self.sizeBlock * height)

        margin = pygame.math.Vector2((self.maxBoardSize.x - self.boardSize.x) / 2, (self.maxBoardSize.y - self.boardSize.y) / 2)

        self.boardPos = pygame.math.Vector2(100, 100) + margin

        default1 = (150, 150, 150)
        default2 = (200, 200, 100)
        zolty = (255, 255, 0)
        czerwony = (255, 0, 0)
        zielony = (0, 255, 0)
        niebieski = (0, 0, 255)
        czarny = (0, 0, 0)
        bialy = (255, 255, 255)
        self.color1 = default1
        self.color2 = default2

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

    def getPos(self, pos):
        positionOnThesScreen = self.boardPos + pygame.math.Vector2(pos.x * self.sizeBlock, pos.y * self.sizeBlock)
        return positionOnThesScreen

