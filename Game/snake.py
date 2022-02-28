import pygame

class Snake():
    def __init__(self, game):
        self.game = game
        #print(game.gameBoard.sizeBlock)
        sizeBlock = game.gameBoard.sizeBlock


        self.length = 1
        # pozycja w tablicy początku węża
        self.headFieldPos = pygame.math.Vector2(4, (int)(game.gameBoard.height / 2))
        # pozycja na ekranie
        self.headFieldCord = self.game.gameBoard.boardPos + pygame.math.Vector2(self.headFieldPos.x *sizeBlock, self.headFieldPos.y *sizeBlock)

        self.snake = pygame.Rect(self.headFieldCord.x, self.headFieldCord.y , sizeBlock, sizeBlock)
        print(self.snake.center)

        #print(self.headFieldCord)
        #self.game.gameBoard.boardPos


        self.headPos = pygame.math.Vector2(0, 0)
        #print(self.headFieldPos)
        #self.headPos = pygame.math.Vector2(0, 0)


    def draw(self):
        pygame.draw.rect(self.game.screen, (255 , 0, 0), self.snake)