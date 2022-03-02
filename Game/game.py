from Game.snake import Snake
from Game.board import Board
import pygame
import sys
from pygame import mixer
from Game.food import Food
from Game.direction import Direction
from Game.fruitType import FruitType
from tools import button

class Game():
    def __init__(self):
        #inicjalizacja
        self.clock = pygame.time.Clock()
        self.speed = 4
        self.tps = 100.0
        self.deltaTime = 0.0
        self.isRun = False
        self.result = 0

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.gameBoard = Board(15, 15, self) # width  - max 47 (min - 5)  height - max 35 (min - 5)
                                             # sizeBlock - minimum 20
        print(self.screen.get_width(), self.screen.get_height())

        self.snake = Snake(self)
        self.food = Food(self)
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
        img = pygame.image.load("img/tlo_game.jpg")
        pygame.Surface.blit(self.screen, img, (0, 0))

        while True:
            exit_img = pygame.image.load("img/exit.png")
            exit_button = button.Button(900, 900, exit_img, 0.7)

            # Przycisk exit
            if exit_button.draw(self.screen):
                mixer.music.load("sounds/BG music - menu.mp3")
                mixer.music.play(-1)
                return True

            # obługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mixer.music.load("sounds/BG music - menu.mp3")
                        mixer.music.play(-1)
                        return True
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
                            self.food.spawnAll()
                            self.snake.currentDirection = Direction.right
                            self.snake.turningDirection = Direction.none
                            self.isRun = True

            # obsługa ruchu, stałe wykonywanie niezalezne od fps
            self.deltaTime += (self.clock.tick() / 1000.0)
            self.snake.Move()

            # rysowanie, wyświetlanie
            #self.screen.fill((0, 0, 0))

            self.gameBoard.draw()
            # tymczasowy prostokąt wyznaczający miejsce na informację
            pygame.draw.rect(self.screen, (0 , 255, 0), pygame.Rect(1100, 80, 360, 700))
            self.food.draw()
            self.snake.draw()

            pygame.display.flip()

    def Defeat(self):
        print("Przegrana")
        sys.exit(0)