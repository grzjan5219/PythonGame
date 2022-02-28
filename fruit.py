import random
import pygame

class Food:
    def __init__(self, game, bounds = (1920, 1080), block_size = 20):
        self.game = game
        self.block_size = block_size
        self.bounds = bounds
        self.color = (255, 255, 255)
        self.x = None
        self.y = None
        self.respawn()

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        blocks_in_x = (self.bounds[0])/self.block_size
        blocks_in_y = (self.bounds[1])/self.block_size
        self.x = random.randint(0, blocks_in_x - 10) * self.block_size
        self.y = random.randint(0, blocks_in_y - 10) * self.block_size