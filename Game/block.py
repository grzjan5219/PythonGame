import pygame
import random
from Game.blockType import BlockType
from Game.blockDirection import BlockDirection
from pygame import mixer

class Block():
    def __init__(self, game):
        self.game = game
        self.commonBlockImage = pygame.transform.scale(pygame.image.load("img/cytryna.png"), (self.game.gameBoard.sizeBlock, self.game.gameBoard.sizeBlock))
        self.blocks = []

    def spawn(self):
        for block in self.blocks:
            while True:
                x = random.randint(0, self.game.gameBoard.width - 1)
                y = random.randint(0, self.game.gameBoard.height - 1)

                if self.game.gameBoard.fields[x][y].isFree and self.game.gameBoard.fields[x][y].blockType == BlockType.none:
                    block.changePos(x, y)
                    self.game.gameBoard.fields[x][y].blockType = BlockType.common
                    self.game.gameBoard.fields[x][y].block = block
                    break

    def respawn(self, block):
        self.game.gameBoard.fields[block.x][block.y].blockType = BlockType.none
        while True:
            x = random.randint(0, self.game.gameBoard.width - 1)
            y = random.randint(0, self.game.gameBoard.height - 1)

            if self.game.gameBoard.fields[x][y].isFree and self.game.gameBoard.fields[x][y].blockType == BlockType.none:
                block.changePos(x, y)
                self.game.gameBoard.fields[x][y].blockType = block.BlockType
                self.game.gameBoard.fields[x][y].block = block


    def add(self, blockType):
        self.blocks.append(Block(blockType))

    def draw(self):
        if self.game.isRun:
            for block in self.blocks:
                self.game.screen.blit(self.commonBlockImage, self.game.gameBoard.fields[block.x][block.y].block)