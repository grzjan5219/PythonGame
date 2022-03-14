import pygame
from copy import deepcopy
from Game.fruitType import FruitType
from Game.przeszkodaType import PrzeszkodaType
from Game.direction import Direction
from Game.section import Section
from Game.sectionTimeWarp import SectionTimeWarp
from Game.gameMode import GameMode
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

        # przenikanie snake
        self.timeWarp = []

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

        for sectionWarp in self.timeWarp:
            if sectionWarp.index == 0:
                pygame.draw.rect(self.game.screen, self.czarny, sectionWarp.rect)
            else:
                pygame.draw.rect(self.game.screen, self.czerwony, sectionWarp.rect)

    def Move(self):
        while self.game.deltaTime > (1 / self.game.tps):
            self.game.deltaTime -= (1 / self.game.tps)

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
                        #print("usuwanie------------------------------------------------------------")



                #print("midd: ", self.purposeMove.x, self.purposeMove.y)
                #print("przed:", self.purposeMove.x, self.purposeMove.y)

                self.changeBodyPurpose()
                self.changeHeadPurpose()

                if self.removeWarp != None:
                    self.endSnakePos = self.removeWarp.endPos
                    self.timeWarp.remove(self.removeWarp)
                    self.removeWarp = None
                    # print(len(self.timeWarp))

                self.continueWayToPurpose(distanceExcess)

                self.displacementValue -= self.game.gameBoard.sizeBlock
                #print("po:   ", self.purposeMove.x, self.purposeMove.y)
            else:
                self.continueWayToPurpose(self.game.speed)

    def changeHeadPurpose(self):
        if self.isNewSegment:
            self.isNewSegment = False

        #print(self.purposeMove.x, self.purposeMove.y)

        if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruitType != FruitType.none:
            # jest owoc
            if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruitType == FruitType.common:
                self.isNewSegment = True
                self.addSegment()
                self.game.result += 1
                self.game.food.respawn(self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].fruit)

        if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].przeszkodaType != PrzeszkodaType.none:
            if self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].przeszkodaType == PrzeszkodaType.common:
                self.game.Defeat()
                return

        if self.turningDirection == Direction.none:
            self.turningDirection = self.headSection.currentDirection

        if self.turningDirection == Direction.up:
            self.headSection.currentDirection = Direction.up
            self.purposeMove += pygame.math.Vector2(0, -1)
        elif self.turningDirection == Direction.down:
            self.headSection.currentDirection = Direction.down
            self.purposeMove += pygame.math.Vector2(0, 1)
        elif self.turningDirection == Direction.right:
            self.headSection.currentDirection = Direction.right
            #print("dodano")
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
            #print(self.purposeMove)
            self.game.Defeat()
            return

        self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].isFree = False
        #self.game.gameBoard.fields[int(self.purposeMove.x)][int(self.purposeMove.y)].color = (0, 255, 0)
        #print("zajete: ", self.purposeMove)
        self.turningDirection = Direction.none
        #print("po: ", self.purposeMove.x, self.purposeMove.y)

    def changeBodyPurpose(self):
        minus = 1

        if self.isNewSegment:
            # nie przemieszcza nowego segmentu w tej sekcji ruchu
            minus +=1
        else:
            self.game.gameBoard.fields[int(self.endSnakePos.x)][int(self.endSnakePos.y)].isFree = True
            #self.game.gameBoard.fields[int(self.endSnakePos.x)][int(self.endSnakePos.y)].color = (0, 0, 0)

            #print("wolne: ", self.endSnakePos)
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
        self.body.append(deepcopy(self.body[-1]))

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
        if self.headSection.currentDirection == Direction.down:
            self.purposeMove += pygame.math.Vector2(0, -self.game.gameBoard.height)

            screenPos = self.game.gameBoard.getPos(self.purposeMove)

            newSection.currentDirection = Direction.down
            newSection.defaultRect = pygame.Rect(screenPos.x, screenPos.y, self.game.gameBoard.sizeBlock, 0)
            newSection.rect = deepcopy(newSection.defaultRect)
            newSection.endPos = deepcopy(self.purposeMove)
        if self.headSection.currentDirection == Direction.right:
            # nowy cel po lewej stronie
            self.purposeMove += pygame.math.Vector2(-self.game.gameBoard.width, 0)

            screenPos = self.game.gameBoard.getPos(self.purposeMove)

            newSection.currentDirection = Direction.right
            newSection.defaultRect = pygame.Rect(screenPos.x, screenPos.y, 0, self.game.gameBoard.sizeBlock)
            newSection.rect = deepcopy(newSection.defaultRect)
            newSection.endPos = deepcopy(self.purposeMove)
        if self.headSection.currentDirection == Direction.left:
            self.purposeMove += pygame.math.Vector2(self.game.gameBoard.width, 0)

            screenPos = self.game.gameBoard.getPos(self.purposeMove)

            newSection.currentDirection = Direction.left
            newSection.defaultRect = pygame.Rect(screenPos.x + self.game.gameBoard.sizeBlock, screenPos.y, 0, self.game.gameBoard.sizeBlock)
            newSection.rect = deepcopy(newSection.defaultRect)
            newSection.endPos = deepcopy(self.purposeMove)

        self.timeWarp.append(newSection)