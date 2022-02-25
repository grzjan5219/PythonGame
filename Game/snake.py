import pygame

class Snake():
    def __init__(self, game):
        self.game = game
        self.snake = pygame.Rect(200, 200, 25, 25)

    def draw(self):
        pygame.draw.rect(self.game.screen, (255 , 0, 0), self.snake)