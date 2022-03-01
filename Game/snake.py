import pygame
import sys
from Game.direction import Direction

class Snake():
    def __init__(self, game):
        self.game = game
        #print(game.gameBoard.sizeBlock)
        sizeBlock = game.gameBoard.sizeBlock
        self.currentDirection = Direction.none
        self.turningDirection = Direction.none


        self.length = 1
        # pozycja w tablicy początku węża
        self.headFieldPos = pygame.math.Vector2(4, (int)(game.gameBoard.height / 2))
        # pozycja na ekranie
        self.headFieldCord = self.game.gameBoard.boardPos + pygame.math.Vector2(self.headFieldPos.x *sizeBlock, self.headFieldPos.y *sizeBlock)
        self.headSnake = pygame.Rect(self.headFieldCord.x, self.headFieldCord.y , sizeBlock, sizeBlock)

        # cel aktualnej sesji ruchu(taablica pól)
        self.purposeMove = headFieldPos + pygame.math.Vector2(1, 0)

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
                '''#ruch w górę
                if self.previousDirection == Directin.up:
                    # kontynuacja ruchu
                    self.headSnake.y -= self.game.speed
                    if not self.game.gameBoard.fields[int(self.headFieldPos.x)][int(self.headFieldPos.y)].block.collidepoint(self.headSnake.midtop):
                        if self.headFieldPos.y - 1 >= 0:
                            self.headFieldPos.y -= 1
                        else:
                            self.game.Defeat()
                else:  # wykonanie skrętu
                    if self.previousDirection == Direction.right:
                        # poprzednio w prawo
                        # w kolejnym będzie skręt
                        if self.headSnake.midright > self.game.gameBoard.fields[int(self.headFieldPos.x)][int(self.headFieldPos.y)].block.centerx:
                            pass
                        else: # w obecnym jest skręt
                            pass

                    if self.previousDirection == Direction.left:
                        # poprzednio w lewo
                        pass


'''
            elif self.currentDirection == Direction.down:
                pass
                #ruch w dół
            elif self.currentDirection == Direction.right:
                if self.headSnake.centerx + self.game.speed >= self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].block.centerx:
                    #dotarło do celu
                    #obliczenie różnicy skrętu
                    distanceToTarget = self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].block.centerx - self.headSnake.centerx
                    distanceExcess = self.game.speed - distanceToTarget
                    #ustalenie nowego celu


                    # dodanie przemieszczenia
                    self.headSnake.x += distanceToTarget
                    self.addDisplacement(self.turningDirection, distanceExcess)
                else:
                    # kontynuacja drogi do celu
                    self.headSnake.x += self.game.speed
            elif self.currentDirection == Direction.left:
                pass
                #ruch w lewo
            elif self.currentDirection == Direction.none:
                pass
                # brak ruchu

    def addDisplacement(self, direction, value):
        match direction:
            case Direction.up:
                self.headSnake.x -= value
            case Direction.down:
                self.headSnake.x += value
            case Direction.right:
                self.headSnake.y += value
            case Direction.left:
                self.headSnake.y -= value
