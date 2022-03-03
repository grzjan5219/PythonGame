import pygame
from copy import deepcopy
from Game.fruitType import FruitType
from Game.direction import Direction
from Game.section import Section

class Snake():
    def __init__(self, game):
        self.game = game
        #pozycja snake na planszy
        self.headFieldPos = pygame.math.Vector2(2, (int)(game.gameBoard.height / 2))
        #pozycja snake na ekranie
        self.headFieldCord = self.game.gameBoard.boardPos + pygame.math.Vector2(self.headFieldPos.x * game.gameBoard.sizeBlock, self.headFieldPos.y * game.gameBoard.sizeBlock)
        self.isNewSegment = False

        #początek snake
        self.headSection = Section()
        self.headSection.currentDirection = Direction.none
        self.headSection.turningDirection = Direction.none
        self.headSection.rect = pygame.Rect(self.headFieldCord.x, self.headFieldCord.y, game.gameBoard.sizeBlock, game.gameBoard.sizeBlock)
        self.headSection.purposeMove = self.headFieldPos + pygame.math.Vector2(1, 0)

        #ciało snake
        self.body = [self.headSection]
        self.addSegment()
        self.body[1].rect.x -= game.gameBoard.sizeBlock
        self.body[1].purposeMove.x -= 1
        self.body[1].currentDirection = Direction.right

        # koniec snake
        self.endSnakePos = pygame.math.Vector2(1, self.headFieldPos.y)

        self.zolty = (255, 255, 0)
        self.czerwony = (255, 0, 0)
        self.zielony = (0, 255, 0)
        self.niebieski = (0, 0, 255)
        self.czarny = (0, 0, 0)
        self.bialy = (255, 255, 255)

    def draw(self):
        for section in self.body:
            pygame.draw.rect(self.game.screen, self.czerwony, section.rect)

    def Move(self):
        while self.game.deltaTime > (1 / self.game.tps):
            self.game.deltaTime -= (1 / self.game.tps)

            if self.headSection.currentDirection == Direction.up:
                if self.headSection.rect.centery - self.game.speed <= self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][int(self.headSection.purposeMove.y)].block.centery:
                    distanceToTarget = self.headSection.rect.centery - self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][int(self.headSection.purposeMove.y)].block.centery
                    distanceExcess = self.game.speed - distanceToTarget

                    self.changeBodyPurpose(distanceToTarget, distanceExcess)
                    self.changeHeadPurpose(distanceExcess)
                    self.headSection.rect.y -= distanceToTarget
                else:
                    self.continueWayToPurpose(Direction.up)
            elif self.headSection.currentDirection == Direction.down:
                if self.headSection.rect.centery + self.game.speed >= self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][
                    int(self.headSection.purposeMove.y)].block.centery:
                    distanceToTarget = self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][
                                           int(self.headSection.purposeMove.y)].block.centery - self.headSection.rect.centery
                    distanceExcess = self.game.speed - distanceToTarget
                    self.changeBodyPurpose(distanceToTarget, distanceExcess)
                    self.changeHeadPurpose(distanceExcess)
                    self.headSection.rect.y += distanceToTarget
                else:
                    self.continueWayToPurpose(Direction.down)
            elif self.headSection.currentDirection == Direction.right:

                if self.headSection.rect.centerx + self.game.speed >= self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][int(self.headSection.purposeMove.y)].block.centerx:
                    # dotarło do celu
                    # obliczenie różnicy skrętu
                    distanceToTarget = self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][int(self.headSection.purposeMove.y)].block.centerx - self.headSection.rect.centerx
                    distanceExcess = self.game.speed - distanceToTarget
                    # ustalenie nowego celu
                    self.changeBodyPurpose(distanceToTarget, distanceExcess)
                    self.changeHeadPurpose(distanceExcess)
                    # dodanie przemieszczenia
                    self.headSection.rect.x += distanceToTarget
                else:
                    # kontynuacja drogi do celu
                    self.continueWayToPurpose(Direction.right)
            elif self.headSection.currentDirection == Direction.left:
                if self.headSection.rect.centerx - self.game.speed <= self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][
                    int(self.headSection.purposeMove.y)].block.centerx:
                    distanceToTarget = self.headSection.rect.centerx - self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][
                        int(self.headSection.purposeMove.y)].block.centerx
                    distanceExcess = self.game.speed - distanceToTarget
                    self.changeBodyPurpose(distanceToTarget, distanceExcess)
                    self.changeHeadPurpose(distanceExcess)
                    self.headSection.rect.x -= distanceToTarget
                else:
                    self.continueWayToPurpose(Direction.left)
            elif self.headSection.currentDirection == Direction.none:
                # brak ruchu
                pass

    def changeHeadPurpose(self, value):
        if self.headSection.turningDirection == Direction.none:  # brak zmiany kierunku
            self.headSection.turningDirection = self.headSection.currentDirection

        if self.isNewSegment:
            self.isNewSegment = False

        if self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][int(self.headSection.purposeMove.y)].fruitType != FruitType.none:
            # jest owoc
            if self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][int(self.headSection.purposeMove.y)].fruitType == FruitType.common:
                self.isNewSegment = True
                self.addSegment()
                self.game.result += 1
                self.game.food.respawn(self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][int(self.headSection.purposeMove.y)].fruit)

        if self.headSection.turningDirection == Direction.up:
            self.headSection.currentDirection = Direction.up
            self.headSection.rect.y -= value
            self.headSection.purposeMove += pygame.math.Vector2(0, -1)
        elif self.headSection.turningDirection == Direction.down:
            self.headSection.currentDirection = Direction.down
            self.headSection.rect.y += value
            self.headSection.purposeMove += pygame.math.Vector2(0, +1)
        elif self.headSection.turningDirection == Direction.right:
            self.headSection.currentDirection = Direction.right
            self.headSection.rect.x += value
            self.headSection.purposeMove += pygame.math.Vector2(+1, 0)
        elif self.headSection.turningDirection == Direction.left:
            self.headSection.currentDirection = Direction.left
            self.headSection.rect.x -= value
            self.headSection.purposeMove += pygame.math.Vector2(-1, 0)

        if not self.game.gameBoard.isExistField(self.headSection.purposeMove) or not self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][int(self.headSection.purposeMove.y)].isFree:
            self.game.Defeat()

        self.game.gameBoard.fields[int(self.headSection.purposeMove.x)][int(self.headSection.purposeMove.y)].isFree = False
        self.headSection.turningDirection = Direction.none

    def changeBodyPurpose(self, distanceToTarget, distanceExcess):

        minus = 1

        if self.isNewSegment:
            # nie przemieszcza nowego segmentu w tej sekcji ruchu
            minus +=1
        else:
            self.game.gameBoard.fields[int(self.endSnakePos.x)][int(self.endSnakePos.y)].isFree = True
            self.endSnakePos = self.body[-1].purposeMove


        for i in range(len(self.body) - minus, 0, -1):
            if self.body[i].currentDirection == Direction.up:
                self.body[i].rect.y -= distanceToTarget
            elif self.body[i].currentDirection == Direction.down:
                self.body[i].rect.y += distanceToTarget
            elif self.body[i].currentDirection == Direction.right:
                self.body[i].rect.x += distanceToTarget
            elif self.body[i].currentDirection == Direction.left:
                self.body[i].rect.x -= distanceToTarget

            self.addExcessToBody(i, distanceExcess)
            self.body[i].purposeMove = deepcopy(self.body[i - 1].purposeMove)
            self.body[i].currentDirection = deepcopy(self.body[i - 1].currentDirection)
            self.body[i].turningDirection = deepcopy(self.body[i - 1].turningDirection)

    def addExcessToBody(self, i, value):
        if self.body[i].turningDirection == Direction.up:
            self.body[i].rect.y -= value
        elif self.body[i].turningDirection == Direction.down:
            self.body[i].rect.y += value
        elif self.body[i].turningDirection == Direction.right:
            self.body[i].rect.x += value
        elif self.body[i].turningDirection == Direction.left:
            self.body[i].rect.x -= value

    def continueWayToPurpose(self, direction):
        minus = 0
        if self.isNewSegment:
            minus = 1

        for i in range(0, len(self.body) - minus):
            if self.body[i].currentDirection == Direction.up:
                self.body[i].rect.y -= self.game.speed
            if self.body[i].currentDirection == Direction.down:
                self.body[i].rect.y += self.game.speed
            if self.body[i].currentDirection == Direction.right:
                self.body[i].rect.x += self.game.speed
            if self.body[i].currentDirection == Direction.left:
                self.body[i].rect.x -= self.game.speed

    def addSegment(self):
        # dodaje segment do snake
        self.body.append(deepcopy(self.body[-1]))
        