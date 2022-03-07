import pygame
from copy import deepcopy
from Game.fruitType import FruitType
from Game.direction import Direction
from Game.section import Section
from collections import deque

class Snake():
    def __init__(self, game):
        self.game = game
        #pozycja snake na planszy
        self.headFieldPos = pygame.math.Vector2(2, (int)(game.gameBoard.height / 2))
        #pozycja snake na ekranie
        self.headFieldCord = self.game.gameBoard.boardPos + pygame.math.Vector2(self.headFieldPos.x * game.gameBoard.sizeBlock, self.headFieldPos.y * game.gameBoard.sizeBlock)
        self.isNewSegment = False

        #print("rozmiar: ", game.gameBoard.sizeBlock)

        #początek snake
        self.purposeMove = self.headFieldPos + pygame.math.Vector2(1, 0)
        #self.turningDirection = Direction.none
        self.headSection = Section()
        self.headSection.currentDirection = Direction.right
        self.headSection.rect = pygame.Rect(self.headFieldCord.x, self.headFieldCord.y, game.gameBoard.sizeBlock, game.gameBoard.sizeBlock)

        #ciało snake
        self.body = [self.headSection]
        self.addSegment()
        self.body[1].rect.x -= game.gameBoard.sizeBlock

        # koniec snake
        self.endSnakePos = pygame.math.Vector2(1, self.headFieldPos.y)

        self.zolty = (255, 255, 0)
        self.czerwony = (255, 0, 0)
        self.zielony = (0, 255, 0)
        self.niebieski = (0, 0, 255)
        self.czarny = (0, 0, 0)
        self.bialy = (255, 255, 255)

    def draw(self):
        pygame.draw.rect(self.game.screen, self.czarny, self.headSection.rect)

        for i in range(1, len(self.body)):
            pygame.draw.rect(self.game.screen, self.czerwony, self.body[i].rect)

    def Move(self):
        while self.game.deltaTime > (1 / self.game.tps):
            self.game.deltaTime -= (1 / self.game.tps)

            if self.headSection.currentDirection == Direction.up:
                if self.headSection.rect.centery - self.game.speed <= self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].block.centery:

                    distanceToTarget = self.headSection.rect.centery - self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].block.centery
                    distanceExcess = self.game.speed - distanceToTarget

                    self.continueWayToPurpose(distanceToTarget)
                    self.changeBodyPurpose()
                    self.changeHeadPurpose()
                    self.continueWayToPurpose(distanceExcess)
                else:
                    self.continueWayToPurpose(self.game.speed)
            elif self.headSection.currentDirection == Direction.down:
                if self.headSection.rect.centery + self.game.speed >= self.game.gameBoard.fields[int(self.purposeMove.x)][
                    int(self.purposeMove.y)].block.centery:
                    distanceToTarget = self.game.gameBoard.fields[int(self.purposeMove.x)][
                                           int(self.purposeMove.y)].block.centery - self.headSection.rect.centery
                    distanceExcess = self.game.speed - distanceToTarget

                    self.continueWayToPurpose(distanceToTarget)
                    self.changeBodyPurpose()
                    self.changeHeadPurpose()
                    self.continueWayToPurpose(distanceExcess)
                else:
                    self.continueWayToPurpose(self.game.speed)
            elif self.headSection.currentDirection == Direction.right:

                if self.headSection.rect.centerx + self.game.speed >= self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].block.centerx:
                    # dotarło do celu
                    # obliczenie różnicy skrętu
                    distanceToTarget = self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].block.centerx - self.headSection.rect.centerx
                    distanceExcess = self.game.speed - distanceToTarget

                    self.continueWayToPurpose(distanceToTarget)
                    self.changeBodyPurpose()
                    self.changeHeadPurpose()
                    self.continueWayToPurpose(distanceExcess)
                else:
                    # kontynuacja drogi do celu
                    self.continueWayToPurpose(self.game.speed)
            elif self.headSection.currentDirection == Direction.left:
                if self.headSection.rect.centerx - self.game.speed <= self.game.gameBoard.fields[int(self.purposeMove.x)][
                    int(self.purposeMove.y)].block.centerx:
                    distanceToTarget = self.headSection.rect.centerx - self.game.gameBoard.fields[int(self.purposeMove.x)][
                        int(self.purposeMove.y)].block.centerx
                    distanceExcess = self.game.speed - distanceToTarget

                    self.continueWayToPurpose(distanceToTarget)
                    self.changeBodyPurpose()
                    self.changeHeadPurpose()
                    self.continueWayToPurpose(distanceExcess)
                else:
                    self.continueWayToPurpose(self.game.speed)

    def changeHeadPurpose(self):
        if self.isNewSegment:
            self.isNewSegment = False

        if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruitType != FruitType.none:
            # jest owoc
            if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruitType == FruitType.common:
                self.isNewSegment = True
                self.addSegment()
                self.game.result += 1
                self.game.food.respawn(self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruit)

        if self.turningDirection == Direction.none:
            self.turningDirection = self.headSection.currentDirection

        if self.turningDirection == Direction.up:
            print("gura")
            self.headSection.currentDirection = Direction.up
            self.purposeMove += pygame.math.Vector2(0, -1)
        elif self.turningDirection == Direction.down:
            self.headSection.currentDirection = Direction.down
            self.purposeMove += pygame.math.Vector2(0, 1)
        elif self.turningDirection == Direction.right:
            print("prawo")
            self.headSection.currentDirection = Direction.right
            self.purposeMove += pygame.math.Vector2(1, 0)
        elif self.turningDirection == Direction.left:
            self.headSection.currentDirection = Direction.left
            self.purposeMove += pygame.math.Vector2(-1, 0)

        if not self.game.gameBoard.isExistField(self.purposeMove) or not self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].isFree:
            self.game.Defeat()
            return

        self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].isFree = False
        self.turningDirection = Direction.none

    def changeBodyPurpose(self):
        minus = 1

        if self.isNewSegment:
            # nie przemieszcza nowego segmentu w tej sekcji ruchu
            minus +=1
        else:
            self.game.gameBoard.fields[int(self.endSnakePos.x)][int(self.endSnakePos.y)].isFree = True
            if self.body[-1].currentDirection == Direction.up:
                self.endSnakePos += pygame.math.Vector2(0, -1)
            if self.body[-1].currentDirection == Direction.down:
                self.endSnakePos += pygame.math.Vector2(0, 1)
            if self.body[-1].currentDirection == Direction.right:
                self.endSnakePos += pygame.math.Vector2(1,0)
            if self.body[-1].currentDirection == Direction.left:
                self.endSnakePos += pygame.math.Vector2(-1, 0)


        for i in range(len(self.body) - minus, 0, -1):
            self.body[i].currentDirection = self.body[i - 1].currentDirection

    def continueWayToPurpose(self, value):
        minus = 0
        if self.isNewSegment:
            minus = 1

        for i in range(0, len(self.body) - minus):
            if self.body[i].currentDirection == Direction.up:
                self.body[i].rect.y -= value
            if self.body[i].currentDirection == Direction.down:
                self.body[i].rect.y += value
            if self.body[i].currentDirection == Direction.right:
                self.body[i].rect.x += value
            if self.body[i].currentDirection == Direction.left:
                self.body[i].rect.x -= value

    def addSegment(self):
        # dodaje segment do snake
        self.body.append(deepcopy(self.body[-1]))