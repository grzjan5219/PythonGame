from Game.snake import Snake
from Game.board import Board
import pygame
import sys
from pygame import mixer
from Game.fruit import Fruit
from Game.direction import Direction

class Game():
    def __init__(self):
        #inicjalizacja
        self.clock = pygame.time.Clock()
        self.speed = 4
        self.tps = 100.0
        self.deltaTime = 0.0
        self.isRun = False

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.gameBoard = Board(15, 15, self) # width  - max 47 (min - 5)  height - max 35 (min - 5)
                                             # sizeBlock - minimum 20

        self.snake = Snake(self)
        self.fruit = Fruit(self)
        pygame.display.set_caption("Snake")

        # muzyka w tle
        mixer.music.load("sounds/BG music - game.mp3")
        mixer.music.play(-1)
        mixer.music.set_volume(0.1)

    def Start(self):
        img = pygame.image.load("img/tlo.jpg")
        while True:
            # obługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake.currentDirection != Direction.down:
                        if self.snake.turningDirection == Direction.none:
                            self.snake.turningDirection = Direction.up
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake.currentDirection != Direction.up:
                        if self.snake.turningDirection == Direction.none:
                            self.snake.turningDirection = Direction.down
                    if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.snake.currentDirection != Direction.right:
                        if self.snake.turningDirection == Direction.none:
                            self.snake.turningDirection = Direction.left
                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.snake.currentDirection != Direction.left:
                        if self.snake.turningDirection == Direction.none:
                            self.snake.turningDirection = Direction.right
                    if event.key == pygame.K_SPACE:
                        if self.isRun == False:
                            print("Start")
                            self.fruit.spawn()
                            self.snake.currentDirection = Direction.right
                            self.snake.turningDirection = Direction.none
                            self.isRun = True

            # obsługa ruchu, stałe wykonywanie niezalezne od fps
            self.deltaTime += (self.clock.tick() / 1000.0)
            self.snake.Move()

            # rysowanie, wyświetlanie
            #self.screen.fill((0, 0, 0))

            pygame.Surface.blit(self.screen, img, (0, 0))

            self.gameBoard.draw()
            # tymczasowy prostokąt wyznaczający miejsce na informację
            pygame.draw.rect(self.screen, (0 , 255, 0), pygame.Rect(1100, 80, 360, 700))

            self.snake.draw()

            pygame.display.flip()

    def Defeat(self):
        print("Przegrana")
        sys.exit(0)