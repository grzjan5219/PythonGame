import pygame
from Game.field import Field

class Board():
    def __init__(self, width, height, game):
        # width - liczba kwadracików w szerokości(x)
        # height - liczba kwadracików w wysokości(y)
        self.width = width
        self.height = height
        self.game = game
        self._fields = [[None] * height] * width # dwuwymiarowa tablica pól planszy

        coordinateX = 80
        coordinateY = 80

        maxWidth = 1100
        maxHeight = 700

        self.sizeBlock = int(min((maxWidth / width), (maxHeight / height)))
        print(sizeBlock)

        for x in range(width):
            coordinateY = 80
            self._fields[x] = [None] * height
            for y in range(height):
                self._fields[x][y] = Field()
                self._fields[x][y].block = pygame.Rect(coordinateX, coordinateY, sizeBlock, sizeBlock)
                coordinateY += sizeBlock
            coordinateX += sizeBlock

    def draw(self):
        color1 = (150 , 150, 150)
        color2 = (200 , 200, 100)
        zmiana = True

        for x in range(self.width):
            for y in range(self.height):
                #print(self._fields[x][y].rect.x, self._fields[x][y].rect.y)
                if zmiana == True:
                    pygame.draw.rect(self.game.screen, color1, self._fields[x][y].block)
                    zmiana = False
                else:
                    pygame.draw.rect(self.game.screen, color2, self._fields[x][y].block)
                    zmiana = True


