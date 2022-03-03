import random
import pygame
from Game.snake import Snake

class Food():
    def __init__(self, game, bounds = (1920, 1080), block_size = 20):
        self.respawn()

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, self.block_size, self.block_size))
        self.snake = Snake(self)
        if self.snake.snake_position[0] == self.x and self.snake.snake_position[1] == self.y:
            pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, self.block_size, self.block_size))
        else:
            self.respawn()

    def respawn(self):
        self.x = random.randint(0, self.blocks_in_x - 20) * self.block_size
        self.y = random.randint(0, self.blocks_in_y - 20) * self.block_size