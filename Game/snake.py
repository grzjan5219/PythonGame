import copy

import pygame
from copy import deepcopy
from Game.fruitType import FruitType
from Game.direction import Direction
from Game.section import Section
from Game.sectionTimeWarp import SectionTimeWarp
from Game.gameMode import GameMode
from Game.turn import Turn
from collections import deque

class Snake():
    def __init__(self, game):
        self.game = game
        #pozycja snake na planszy
        self.headFieldPos = pygame.math.Vector2(2, (int)(game.gameBoard.height / 2))
        #pozycja snake na ekranie
        self.headFieldCord = self.game.gameBoard.boardPos + pygame.math.Vector2(self.headFieldPos.x * game.gameBoard.sizeBlock, self.headFieldPos.y * game.gameBoard.sizeBlock)
        self.isNewSegment = False
        self.displacementValue = 0
        self.removeWarp = None
        self.turnings = deque()

        #początek snake
        self.purposeMove = self.headFieldPos + pygame.math.Vector2(1, 0)
        self.headSection = Section()
        self.headSection.currentDirection = Direction.right
        self.headSection.rect = pygame.Rect(self.headFieldCord.x, self.headFieldCord.y, game.gameBoard.sizeBlock, game.gameBoard.sizeBlock)

        #ciało snake
        self.body = [self.headSection]
        self.addSegment()
        self.body[1].rect.x -= game.gameBoard.sizeBlock

        self.tailSection = self.body[1]

        # koniec snake
        self.endSnakePos = pygame.math.Vector2(1, self.headFieldPos.y)

        # przenikanie snake
        self.timeWarp = []

        self.headImage = {}
        self.bodyImage = {}
        self.tailImage = {}

        self.headImage[Direction.up] = pygame.transform.scale(pygame.image.load("img/snake/head_up.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.headImage[Direction.down] = pygame.transform.scale(pygame.image.load("img/snake/head_down.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.headImage[Direction.right] = pygame.transform.scale(pygame.image.load("img/snake/head_right.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.headImage[Direction.left] = pygame.transform.scale(pygame.image.load("img/snake/head_left.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))

        self.bodyImage[Direction.up] = pygame.transform.scale(pygame.image.load("img/snake/body_vertical.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.bodyImage[Direction.down] = pygame.transform.scale(pygame.image.load("img/snake/body_vertical.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.bodyImage[Direction.right] = pygame.transform.scale(pygame.image.load("img/snake/body_horizontal.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.bodyImage[Direction.left] = pygame.transform.scale(pygame.image.load("img/snake/body_horizontal.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))

        self.tailImage[Direction.up] = pygame.transform.scale(pygame.image.load("img/snake/tail_up.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.tailImage[Direction.down] = pygame.transform.scale(pygame.image.load("img/snake/tail_down.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.tailImage[Direction.right] = pygame.transform.scale(pygame.image.load("img/snake/tail_right.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.tailImage[Direction.left] = pygame.transform.scale(pygame.image.load("img/snake/tail_left.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))

        self.turnLeftUp = pygame.transform.scale(pygame.image.load("img/snake/leftUp.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.turnLeftDown = pygame.transform.scale(pygame.image.load("img/snake/leftDown.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.turnRightUp = pygame.transform.scale(pygame.image.load("img/snake/rightUp.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.turnRightDown = pygame.transform.scale(pygame.image.load("img/snake/rightDown.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))

        self.zolty = (255, 255, 0)
        self.czerwony = (255, 0, 0)
        self.zielony = (0, 255, 0)
        self.niebieski = (0, 0, 255)
        self.czarny = (0, 0, 0)
        self.bialy = (255, 255, 255)

    def draw(self):
        self.drawSection(self.headImage, self.headSection)

        for i in range(1, len(self.body) - 1):
            self.drawSection(self.bodyImage, self.body[i])

        self.drawSection(self.tailImage, self.tailSection)

        for sectionWarp in self.timeWarp:
            if sectionWarp.index == 0:
                self.drawSectionInvers(self.headImage, sectionWarp)
            elif sectionWarp.index == len(self.body)-1:
                self.drawSectionInvers(self.tailImage, sectionWarp)
            else:
                self.drawSectionInvers(self.bodyImage, sectionWarp)

        for turn in self.turnings:
            pygame.draw.rect(self.game.screen, self.game.gameBoard.fields[int(turn.pos.x)][int(turn.pos.y)].color, self.game.gameBoard.fields[int(turn.pos.x)][int(turn.pos.y)].block)
            self.game.screen.blit(turn.image, turn.globalPos)

    def drawSection(self, image, section):
       if section.currentDirection == Direction.left:
           self.game.screen.blit(image[section.currentDirection], (section.rect.x, section.rect.y), (self.game.gameBoard.sizeBlock - section.rect.width, 0, section.rect.width, section.rect.height))
       elif section.currentDirection == Direction.up:
           self.game.screen.blit(image[section.currentDirection], (section.rect.x, section.rect.y), (0, self.game.gameBoard.sizeBlock - section.rect.height, section.rect.width, section.rect.height))
       else:
           self.game.screen.blit(image[section.currentDirection], (section.rect.x, section.rect.y), (0, 0, section.rect.width, section.rect.height))

    def drawSectionInvers(self, image, section):
        if section.currentDirection == Direction.right:
            self.game.screen.blit(image[section.currentDirection],(section.rect.x, section.rect.y), (self.game.gameBoard.sizeBlock - section.rect.width, 0, section.rect.width,section.rect.height))
        elif section.currentDirection == Direction.down:
            self.game.screen.blit(image[section.currentDirection], (section.rect.x, section.rect.y), (0, self.game.gameBoard.sizeBlock - section.rect.height, section.rect.width, section.rect.height))
        else:
            self.game.screen.blit(image[section.currentDirection],(section.rect.x, section.rect.y),(0, 0, section.rect.width, section.rect.height))

    def Move(self):
        while self.game.deltaTime > (1 / self.game.tps):
            self.game.deltaTime -= (1 / self.game.tps)
            self.game.food.tick()

            self.displacementValue += self.game.speed

            if self.displacementValue >= self.game.gameBoard.sizeBlock:
                distanceExcess = self.displacementValue - self.game.gameBoard.sizeBlock
                distanceToTarget = self.game.speed - distanceExcess

                self.continueWayToPurpose(distanceToTarget)

                for sectionWarp in self.timeWarp:
                    self.body[sectionWarp.index].rect = sectionWarp.rect
                    sectionWarp.index += 1

                    if sectionWarp.index == len(self.body):
                        self.removeWarp = sectionWarp
                        continue

                    sectionWarp.rect = deepcopy(sectionWarp.defaultRect)

                self.changeBodyPurpose()
                self.changeHeadPurpose()

                if self.removeWarp != None:
                    self.endSnakePos = self.removeWarp.endPos
                    self.timeWarp.remove(self.removeWarp)
                    self.removeWarp = None

                    if len(self.turnings) > 0 and self.turnings[0].pos.x == self.endSnakePos.x and self.turnings[
                        0].pos.y == self.endSnakePos.y:
                        self.turnings.popleft()

                self.continueWayToPurpose(distanceExcess)

                self.displacementValue -= self.game.gameBoard.sizeBlock
            else:
                self.continueWayToPurpose(self.game.speed)

    def changeHeadPurpose(self):
        if self.isNewSegment:
            self.isNewSegment = False

        if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruitType != FruitType.none:
            if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruitType == FruitType.common:
                self.isNewSegment = True
                self.game.result += 1
                self.tailSection = self.addSegment()
                self.game.food.respawn(self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruit)


        if self.turningDirection == Direction.none:
            self.turningDirection = self.headSection.currentDirection
        elif self.turningDirection != self.headSection.currentDirection:
            newTurn = Turn(copy.deepcopy(self.purposeMove))
            newTurn.globalPos = self.game.gameBoard.getPos(newTurn.pos)

            if self.headSection.currentDirection == Direction.up:
                if self.turningDirection == Direction.left:
                    newTurn.image = self.turnLeftDown
                else:
                    newTurn.image = self.turnRightDown
            elif self.headSection.currentDirection == Direction.down:
                if self.turningDirection == Direction.left:
                    newTurn.image = self.turnLeftUp
                else:
                    newTurn.image = self.turnRightUp
            elif self.headSection.currentDirection == Direction.right:
                if self.turningDirection == Direction.up:
                    newTurn.image = self.turnLeftUp
                else:
                    newTurn.image = self.turnLeftDown
            else:
                if self.turningDirection == Direction.up:
                    newTurn.image = self.turnRightUp
                else:
                    newTurn.image = self.turnRightDown

            self.turnings.append(newTurn)

        if self.turningDirection == Direction.up:
            self.headSection.currentDirection = Direction.up
            self.purposeMove += pygame.math.Vector2(0, -1)
        elif self.turningDirection == Direction.down:
            self.headSection.currentDirection = Direction.down
            self.purposeMove += pygame.math.Vector2(0, 1)
        elif self.turningDirection == Direction.right:
            self.headSection.currentDirection = Direction.right
            self.purposeMove += pygame.math.Vector2(1, 0)
        elif self.turningDirection == Direction.left:
            self.headSection.currentDirection = Direction.left
            self.purposeMove += pygame.math.Vector2(-1, 0)

        if not self.game.gameBoard.isExistField(self.purposeMove):
            if self.game.gameMode == GameMode.standard:
                self.game.Defeat()
                return
            elif self.game.gameMode == GameMode.timeWarp:
                self.timeWarpChange()

        if not self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].isFree:
            self.game.Defeat()
            return

        self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].isFree = False
        self.turningDirection = Direction.none

    def changeBodyPurpose(self):
        minus = 1

        if self.isNewSegment:
            minus +=1
        else:
            self.game.gameBoard.fields[int(self.endSnakePos.x)][int(self.endSnakePos.y)].isFree = True

            if self.body[-1].currentDirection == Direction.up:
                self.endSnakePos += pygame.math.Vector2(0, -1)
            if self.body[-1].currentDirection == Direction.down:
                self.endSnakePos += pygame.math.Vector2(0, 1)
            if self.body[-1].currentDirection == Direction.right:
                self.endSnakePos += pygame.math.Vector2(1, 0)
            if self.body[-1].currentDirection == Direction.left:
                self.endSnakePos += pygame.math.Vector2(-1, 0)

            if len(self.turnings) > 0 and self.turnings[0].pos.x == self.endSnakePos.x and self.turnings[0].pos.y == self.endSnakePos.y:
                self.turnings.popleft()

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

        for sectionWarp in self.timeWarp:
            if sectionWarp.currentDirection == Direction.up:
                sectionWarp.rect.height += value
                sectionWarp.rect.y -= value
                self.body[sectionWarp.index].rect.height -= value
                self.body[sectionWarp.index].rect.y += value
            if sectionWarp.currentDirection == Direction.down:
                sectionWarp.rect.height += value
                self.body[sectionWarp.index].rect.height -= value
            if sectionWarp.currentDirection == Direction.right:
                sectionWarp.rect.width += value
                self.body[sectionWarp.index].rect.width -= value
            if sectionWarp.currentDirection == Direction.left:
                sectionWarp.rect.width += value
                sectionWarp.rect.x -= value
                self.body[sectionWarp.index].rect.width -= value
                self.body[sectionWarp.index].rect.x += value

    def addSegment(self):
        # dodaje segment do snake
        newSection = deepcopy(self.body[-1])
        self.body.append(newSection)
        return newSection

    def timeWarpChange(self):
        # tylko raz wykonuje na początku zakrzywienia

        newSection = SectionTimeWarp()
        newSection.index = 0

        if self.headSection.currentDirection == Direction.up:
            self.purposeMove += pygame.math.Vector2(0, self.game.gameBoard.height)

            screenPos = self.game.gameBoard.getPos(self.purposeMove)

            newSection.currentDirection = Direction.up
            newSection.defaultRect = pygame.Rect(screenPos.x, screenPos.y + self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock, 0)
            newSection.rect = deepcopy(newSection.defaultRect)
            newSection.endPos = deepcopy(self.purposeMove)
        elif self.headSection.currentDirection == Direction.down:
            self.purposeMove += pygame.math.Vector2(0, -self.game.gameBoard.height)

            screenPos = self.game.gameBoard.getPos(self.purposeMove)

            newSection.currentDirection = Direction.down
            newSection.defaultRect = pygame.Rect(screenPos.x, screenPos.y, self.game.gameBoard.sizeBlock, 0)
            newSection.rect = deepcopy(newSection.defaultRect)
            newSection.endPos = deepcopy(self.purposeMove)
        elif self.headSection.currentDirection == Direction.right:
            self.purposeMove += pygame.math.Vector2(-self.game.gameBoard.width, 0)

            screenPos = self.game.gameBoard.getPos(self.purposeMove)

            newSection.currentDirection = Direction.right
            newSection.defaultRect = pygame.Rect(screenPos.x, screenPos.y, 0, self.game.gameBoard.sizeBlock)
            newSection.rect = deepcopy(newSection.defaultRect)
            newSection.endPos = deepcopy(self.purposeMove)
        elif self.headSection.currentDirection == Direction.left:
            self.purposeMove += pygame.math.Vector2(self.game.gameBoard.width, 0)

            screenPos = self.game.gameBoard.getPos(self.purposeMove)

            newSection.currentDirection = Direction.left
            newSection.defaultRect = pygame.Rect(screenPos.x + self.game.gameBoard.sizeBlock, screenPos.y, 0, self.game.gameBoard.sizeBlock)
            newSection.rect = deepcopy(newSection.defaultRect)
            newSection.endPos = deepcopy(self.purposeMove)

        self.timeWarp.append(newSection)