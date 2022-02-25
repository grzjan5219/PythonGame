import random
import pygame

class Food:
    def __init__(self, game, bounds = (1920, 1080), block_size = 20):
        self.game = game
        self.block_size = block_size
        self.bounds = bounds
        self.color = (0, 255, 0)
        self.x = 0;
        self.y = 0;

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        blocks_in_x = (self.bounds[0])/self.block_size
        blocks_in_y = (self.bounds[1])/self.block_size
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size