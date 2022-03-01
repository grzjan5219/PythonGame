import pygame
from fruit import Food
from Game.direction import Direction

class Snake():
    def __init__(self, game):
        self.game = game
        #print(game.gameBoard.sizeBlock)
        sizeBlock = game.gameBoard.sizeBlock

        self.currentDirection = Direction.right
        self.turningDirection = Direction.none

        #snake_position = [200, 200]
        #self.snake_position = snake_position
        #self.snake_body = [[200, 180], [200, 160], [200, 140], [200, 120]]

        #self.snake = pygame.Rect(self.snake_position[0], self.snake_position[1], sizeBlock, sizeBlock)


        self.headFieldPos = pygame.math.Vector2(4, (int)(game.gameBoard.height / 2))
        self.headFieldCord = self.game.gameBoard.boardPos + pygame.math.Vector2(self.headFieldPos.x *sizeBlock, self.headFieldPos.y *sizeBlock)
        self.headSnake = pygame.Rect(self.headFieldCord.x, self.headFieldCord.y, sizeBlock, sizeBlock)

        # cel aktualnej sesji ruchu(taablica pól)
        self.purposeMove = self.headFieldPos + pygame.math.Vector2(1, 0)

        self.direction = Direction.right

        #print(self.snake.centery)

        #print(self.headFieldCord)
        #self.game.gameBoard.boardPos


        self.headPos = pygame.math.Vector2(0, 0)
        #print(self.headFieldPos)
        #self.headPos = pygame.math.Vector2(0, 0)


    def draw(self):
        pygame.draw.rect(self.game.screen, (255 , 0, 0), self.headSnake)
        # UWAGA PLAC BUDOWY NIE WCHODZIC, NIE PYTAC

    def Move(self):

        while self.game.deltaTime > (1 / self.game.tps):

            self.game.deltaTime -= (1 / self.game.tps)

            if self.currentDirection == Direction.up:
                if self.headSnake.centery - self.game.speed <= self.game.gameBoard.fields[int(self.purposeMove.x)][
                    int(self.purposeMove.y)].block.centery:
                    distanceToTarget = self.headSnake.centery - self.game.gameBoard.fields[int(self.purposeMove.x)][
                        int(self.purposeMove.y)].block.centery
                    distanceExcess = self.game.speed - distanceToTarget
                    self.changePurpose(distanceExcess)
                    self.headSnake.y -= distanceToTarget
                else:
                    self.headSnake.y -= self.game.speed

            elif self.currentDirection == Direction.down:
                if self.headSnake.centery + self.game.speed >= self.game.gameBoard.fields[int(self.purposeMove.x)][
                    int(self.purposeMove.y)].block.centery:
                    distanceToTarget = self.game.gameBoard.fields[int(self.purposeMove.x)][
                                           int(self.purposeMove.y)].block.centery - self.headSnake.centery
                    distanceExcess = self.game.speed - distanceToTarget
                    self.changePurpose(distanceExcess)
                    self.headSnake.y += distanceToTarget
                else:
                    self.headSnake.y += self.game.speed
            elif self.currentDirection == Direction.right:

                if self.headSnake.centerx + self.game.speed >= self.game.gameBoard.fields[int(self.purposeMove.x)][
                    int(self.purposeMove.y)].block.centerx:
                    # dotarło do celu
                    # obliczenie różnicy skrętu
                    distanceToTarget = self.game.gameBoard.fields[int(self.purposeMove.x)][
                                           int(self.purposeMove.y)].block.centerx - self.headSnake.centerx
                    distanceExcess = self.game.speed - distanceToTarget
                    # ustalenie nowego celu
                    self.changePurpose(distanceExcess)
                    # dodanie przemieszczenia
                    self.headSnake.x += distanceToTarget
                else:
                    # kontynuacja drogi do celu
                    self.headSnake.x += self.game.speed
            elif self.currentDirection == Direction.left:
                if self.headSnake.centerx - self.game.speed <= self.game.gameBoard.fields[int(self.purposeMove.x)][
                    int(self.purposeMove.y)].block.centerx:
                    distanceToTarget = self.headSnake.centerx - self.game.gameBoard.fields[int(self.purposeMove.x)][
                        int(self.purposeMove.y)].block.centerx
                    distanceExcess = self.game.speed - distanceToTarget
                    # ustalenie nowego celu
                    self.changePurpose(distanceExcess)
                    # dodanie przemieszczenia
                    self.headSnake.x -= distanceToTarget
                else:
                    # kontynuacja drogi do celu
                    self.headSnake.x -= self.game.speed

            elif self.currentDirection == Direction.none:
                pass
                # brak ruchu

    def changePurpose(self, value):
        if self.turningDirection == Direction.none:  # brak zmiany kierunku
            self.turningDirection = self.currentDirection

        match self.turningDirection:
            case Direction.up:
                self.currentDirection = Direction.up
                self.headSnake.y -= value
                self.purposeMove += pygame.math.Vector2(0, -1)
            case Direction.down:
                self.currentDirection = Direction.down
                self.headSnake.y += value
                self.purposeMove += pygame.math.Vector2(0, +1)
            case Direction.right:
                self.currentDirection = Direction.right
                self.headSnake.x += value
                self.purposeMove += pygame.math.Vector2(+1, 0)
            case Direction.left:
                self.currentDirection = Direction.left
                self.headSnake.x -= value
                self.purposeMove += pygame.math.Vector2(-1, 0)

        self.turningDirection = Direction.none