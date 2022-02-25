import pygame
from Game.field import Field

class Board():
    def __init__(self, width, height, game):
        # width - liczba kwadracików w szerokości(x)
        # height - liczba kwadracików w wysokości(y)
        self.width = width
        self.height = height
        self.game = game
        # dwuwymiarowa tablica pól planszy
        self._fields = [[None] * height]*width

        coordinateX = 50
        coordinateY = 50

        for x in range(width):
            coordinateY = 50
            self._fields[x] = [None] * height
            for y in range(height):
                self._fields[x][y] = Field()
                self._fields[x][y].block = pygame.Rect(coordinateX, coordinateY, 30, 30)
                #self._fields[x][y]._rect.x = coordinateX
                #self._fields[x][y]._rect.y = coordinateY
                #print(coordinateX, coordinateY)
                #print(self._fields[x][y].rect.x, self._fields[x][y].rect.y)
                coordinateY += 30
            coordinateX += 30

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


