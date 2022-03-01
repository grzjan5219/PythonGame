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

        #print(margin)
        self.boardPos = pygame.math.Vector2(80, 80) + margin
        #print(self.boardPos)

        fieldPos = copy.deepcopy(self.boardPos)

        for x in range(width):
            fieldPos.y = self.boardPos.y
            self.fields[x] = [None] * height
            for y in range(height):
                self.fields[x][y] = Field()
                self.fields[x][y].block = pygame.Rect(fieldPos.x, fieldPos.y, self.sizeBlock, self.sizeBlock)
                fieldPos.y += self.sizeBlock
            fieldPos.x += self.sizeBlock

    def draw(self):
        color1 = (150 , 150, 150)
        color2 = (200 , 200, 100)
        zmiana = True

        for x in range(self.width):
            for y in range(self.height):
                #print(self._fields[x][y].rect.x, self._fields[x][y].rect.y)
                if zmiana == True:
                    pygame.draw.rect(self.game.screen, color1, self.fields[x][y].block)
                    zmiana = False
                else:
                    pygame.draw.rect(self.game.screen, color2, self.fields[x][y].block)
                    zmiana = True