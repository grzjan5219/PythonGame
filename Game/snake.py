import pygame

class Snake():
    def __init__(self, game):
        self.game = game
        #print(game.gameBoard.sizeBlock)
        sizeBlock = game.gameBoard.sizeBlock

        snake_position = [200, 200]
        snake_body = [[200, 175], [200, 150], [200, 125], [200, 100]]
        self.snake = pygame.Rect(snake_position[0], snake_position[1], sizeBlock-4, sizeBlock-4)
        self.length = 1
        self.headFieldPos = pygame.math.Vector2(4, (int)(game.gameBoard.height / 2))
        self.headFieldCord = self.game.gameBoard.boardPos + pygame.math.Vector2(self.headFieldPos.x *sizeBlock, self.headFieldPos.y *sizeBlock)

        print(self.snake.centery)


        #print(self.headFieldCord)
        #self.game.gameBoard.boardPos


        self.headPos = pygame.math.Vector2(0, 0)
        #print(self.headFieldPos)
        #self.headPos = pygame.math.Vector2(0, 0)


    def draw(self):
        pygame.draw.rect(self.game.screen, (255 , 0, 0), self.snake)