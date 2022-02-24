import random

class Food:
    image = pygame.image.load('img/fruit.png').convert_alpha()
    block_size = None
    x = 0;
    y = 0;
    bounds = None

    def __init__(self, block_size, bounds, image):
        self.block_size = block_size
        self.bounds = bounds
        self.Food.image = Food.image

    def draw(self, game, window):
        game.draw.rect(window, self.Food.image, (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        blocks_x = (self.bounds[0])/self.block_size;
        blocks_y = (self.bounds[1])/self.block_size;
        self.x = random.randint(0, blocks_x - 1) * self.block_size
        self.y = random.randint(0, blocks_y - 1) * self.block_size