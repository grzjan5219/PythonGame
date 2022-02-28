import pygame
from fruit import Food

class Snake():
    def __init__(self, game):
        self.game = game
        #print(game.gameBoard.sizeBlock)
        sizeBlock = game.gameBoard.sizeBlock

        snake_position = [200, 200]
        self.snake_position = snake_position
        self.snake_body = [[200, 180], [200, 160], [200, 140], [200, 120]]
        self.snake = pygame.Rect(self.snake_position[0], self.snake_position[1], sizeBlock, sizeBlock)
        self.headFieldPos = pygame.math.Vector2(4, (int)(game.gameBoard.height / 2))
        self.headFieldCord = self.game.gameBoard.boardPos + pygame.math.Vector2(self.headFieldPos.x *sizeBlock, self.headFieldPos.y *sizeBlock)

        print(self.snake.centery)

        self.food = Food(self)
        self.snake_body.insert(0, list(self.snake_position))
        if self.snake_position[0] == self.food.x and self.snake_position[1] == self.food.y:
            self.food.respawn()
        else:
            self.snake_body.pop()

        #print(self.headFieldCord)
        #self.game.gameBoard.boardPos


        self.headPos = pygame.math.Vector2(0, 0)
        #print(self.headFieldPos)
        #self.headPos = pygame.math.Vector2(0, 0)


    def draw(self):
        pygame.draw.rect(self.game.screen, (255 , 0, 0), self.snake)