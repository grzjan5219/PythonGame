from Game.snake import Snake
from Game.board import Board
import pygame
import sys
from pygame import mixer
from fruit import Food

class Game():
    def __init__(self):
        #inicjalizacja
        self.clock = pygame.time.Clock()
        self.speed = 2
        self.tps = 100.0
        self.deltaTime = 0.0

        #self.food = Food(self)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((600, 600), pygame.SCALED | pygame.RESIZABLE)
        self.gameBoard = Board(47, 35, self) # narazie druga liczba musi być nieparzysta
                                             # width  - max 47 (min - 5)  height - max 35 (min - 5)
                                             # sizeBlock - minimum 20
        self.snake = Snake(self)
        self.food = Food(self)
        pygame.display.set_caption("Snake")

        # muzyka w tle
        mixer.music.load("sounds/BG music - game.mp3")
        mixer.music.play(-1)
        mixer.music.set_volume(0.1)

    def Start(self):
        currentKey = "q"

        while True:
            # obługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_w and currentKey != "s":
                        currentKey = "w"
                    if event.key == pygame.K_s and currentKey != "w":
                        currentKey = "s"
                    if event.key == pygame.K_a and currentKey != "d":
                        currentKey = "a"
                    if event.key == pygame.K_d and currentKey != "a":
                        currentKey = "d"

            # obsługa ruchu
            self.deltaTime += (self.clock.tick() / 1000.0)
            self.Move(currentKey)

            # rysowanie, wyświetlanie
            self.screen.fill((0, 0, 0))

            self.gameBoard.draw()
            pygame.draw.rect(self.screen, (0 , 255, 0), pygame.Rect(1100, 80, 360, 700))

            self.snake.draw()
            self.food.draw()
            #self.food.draw()

            pygame.display.flip()

    def Move(self, key):

        while self.deltaTime > (1 / self.tps):
            self.deltaTime -= (1 / self.tps)

            if key == "q":
                return
            if key == "w":
                self.snake.snake.y -= self.speed
            if key == "s":
                self.snake.snake.y += self.speed
            if key == "a":
                self.snake.snake.x -= self.speed
            if key == "d":
                self.snake.snake.x += self.speed