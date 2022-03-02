import pygame
from Game.fruitType import FruitType
from Game.direction import Direction

class Snake():
    def __init__(self, game):
        self.game = game
        self.currentDirection = Direction.none
        self.turningDirection = Direction.none

        sizeBlock = game.gameBoard.sizeBlock

        #pozycja na planszy
        self.headFieldPos = pygame.math.Vector2(4, (int)(game.gameBoard.height / 2))
        #pzycja na ekranie
        self.headFieldCord = self.game.gameBoard.boardPos + pygame.math.Vector2(self.headFieldPos.x * sizeBlock, self.headFieldPos.y * sizeBlock)
        #początek snake
        self.headSnake = pygame.Rect(self.headFieldCord.x, self.headFieldCord.y, sizeBlock, sizeBlock)

        # cel aktualnej sesji ruchu(taablica pól)
        self.purposeMove = self.headFieldPos + pygame.math.Vector2(1, 0)

    def draw(self):
        pygame.draw.rect(self.game.screen, (255 , 0, 0), self.headSnake)


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

        if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruitType != FruitType.none:
            if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruitType == FruitType.common:
                self.game.result += 1;
                print(self.game.result)
                self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].color = (100, 0, 100)
                #self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruitType = FruitType.none
                self.game.food.respawn(self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruit)

        if self.turningDirection == Direction.up:
            self.currentDirection = Direction.up
            self.headSnake.y -= value
            self.purposeMove += pygame.math.Vector2(0, -1)
        elif self.turningDirection == Direction.down:
            self.currentDirection = Direction.down
            self.headSnake.y += value
            self.purposeMove += pygame.math.Vector2(0, +1)
        elif self.turningDirection == Direction.right:
            self.currentDirection = Direction.right
            self.headSnake.x += value
            self.purposeMove += pygame.math.Vector2(+1, 0)
        elif self.turningDirection == Direction.left:
            self.currentDirection = Direction.left
            self.headSnake.x -= value
            self.purposeMove += pygame.math.Vector2(-1, 0)

        if not self.game.gameBoard.isExistField(self.purposeMove):
            self.game.Defeat()
        self.turningDirection = Direction.none