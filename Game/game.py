from Game.snake import Snake
from Game.board import Board
import pygame
import sys
from pygame import mixer
from Game.food import Food
from Game.direction import Direction
from Game.fruitType import FruitType
from Game.gui import Gui
from tools import button

class Game():
    def __init__(self):
        #inicjalizacja
        self.clock = pygame.time.Clock()
        wolny = 2
        default = 4
        szybki = 6
        bardzo_szybki = 8
        self.speed = default
        self.tps = 100.0
        self.deltaTime = 0.0
        self.isRun = False
        self.result = 0
        # 1200 # 880

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.gameBoard = Board(15, 15, self) # width  - max 60 (min - 5)  height - max 44 (min - 5)
                                             # sizeBlock - minimum 20
        #print(self.screen.get_width(), self.screen.get_height())
        self.background = pygame.image.load("img/tlo_game.jpg")

        self.snake = Snake(self)
        self.food = Food(self)
        self.gui = Gui(self)
        # trzy owoce
        self.food.add(FruitType.common)
        self.food.add(FruitType.common)
        self.food.add(FruitType.common)
        pygame.display.set_caption("Snake")

        # muzyka w tle
        mixer.music.load("sounds/BG music - game.mp3")
        mixer.music.play(-1)
        mixer.music.set_volume(0.1)

    def Start(self):

        while True:
            # rysowanie, wyświetlanie
            pygame.Surface.blit(self.screen, self.background, (0, 0))

            # obługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mixer.music.load("sounds/BG music - menu.mp3")
                        mixer.music.play(-1)
                        return True
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake.headSection.currentDirection != Direction.down:
                        if self.snake.headSection.turningDirection == Direction.none:
                            self.snake.headSection.turningDirection = Direction.up
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake.headSection.currentDirection != Direction.up:
                        if self.snake.headSection.turningDirection == Direction.none:
                            self.snake.headSection.turningDirection = Direction.down
                    if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.snake.headSection.currentDirection != Direction.right:
                        if self.snake.headSection.turningDirection == Direction.none:
                            self.snake.headSection.turningDirection = Direction.left
                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.snake.headSection.currentDirection != Direction.left:
                        if self.snake.headSection.turningDirection == Direction.none:
                            self.snake.headSection.turningDirection = Direction.right
                    if event.key == pygame.K_SPACE:
                        if self.isRun == False:
                            print("Start")
                            self.food.spawn()
                            self.snake.headSection.turningDirection = Direction.none
                            self.isRun = True
                            self.clock.tick()

            # obsługa ruchu, stałe wykonywanie niezalezne od fps
            if self.isRun:
                self.deltaTime += (self.clock.tick() / 1000.0)
                self.snake.Move()

            self.gameBoard.draw()
            # tymczasowy prostokąt wyznaczający miejsce na informację
            pygame.draw.rect(self.screen, (0 , 255, 0), pygame.Rect(1400, 100, 420, 880))
            #pygame.draw.rect(self.screen, (0 , 255, 0), pygame.Rect(100, 100, 1200, 880))
            self.food.draw()
            self.snake.draw()
            self.gui.draw()

            pygame.display.flip()

    def Defeat(self):
        print("Przegrana punkty: ", self.result)
        self.snake.headSection.currentDirection = Direction.none
        self.isRun = False
        #sys.exit(0)

    def Reset(self):
        pass