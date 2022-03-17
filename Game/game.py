from Game.snake import Snake
from Game.board import Board
import pygame
import sys
from pygame import mixer
from Game.food import Food
from Game.gui import Gui
from Game.direction import Direction
from Game.fruitType import FruitType
from Game.gameMode import GameMode
from tools import Buttonhover2
from Archive.przeszkodaType import PrzeszkodaType
from os import path
import os

#plik który przechowuje najwyższy wynik
HS_FILE = "highscore.txt"

class Game():
    def __init__(self, gamemode, width, height):
        #inicjalizacja
        self.clock = pygame.time.Clock()
        self.speed = 4
        self.tps = 100.0
        self.deltaTime = 0.0
        self.paused = False
        self.isRun = False
        self.result = 0

        # to jest potrzebne do animowanego tła + TEKST
        self.win = pygame.display.set_mode((1920, 1080))
        self.bg_img = pygame.image.load(os.path.join("img/tlo_wide.jpg"))
        self.bg = pygame.transform.scale(self.bg_img, (3840, 1080))
        self.width = 3840
        self.i = 0
        self.GAME_OVER = pygame.image.load("img/okno_game_over.png")

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.gameBoard = Board(width, height, self) # width  - max 60 (min - 5)  height - max 44 (min - 5)
                                             # sizeBlock - minimum 20
        # tryb gry
        self.gameMode = gamemode

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
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def Start(self):

        while True:
            pause_font = pygame.font.Font('customFont/upheavtt.ttf', 100)
            pause = pause_font.render("Paused", 1, (0, 0, 0))

            # obługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused
                    elif self.paused is True:
                        continue
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and self.snake.headSection.currentDirection != Direction.down:
                        if self.snake.turningDirection == Direction.none:
                            self.snake.turningDirection = Direction.up
                    if (event.key == pygame.K_s or event.key == pygame.K_DOWN) and self.snake.headSection.currentDirection != Direction.up:
                        if self.snake.turningDirection == Direction.none:
                            self.snake.turningDirection = Direction.down
                    if (event.key == pygame.K_a or event.key == pygame.K_LEFT) and self.snake.headSection.currentDirection != Direction.right:
                        if self.snake.turningDirection == Direction.none:
                            self.snake.turningDirection = Direction.left
                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and self.snake.headSection.currentDirection != Direction.left:
                        if self.snake.turningDirection == Direction.none:
                            self.snake.turningDirection = Direction.right
                    if event.key == pygame.K_SPACE:
                        if self.isRun == False:
                            self.food.spawn()
                            self.snake.turningDirection = Direction.none
                            self.isRun = True
                            self.clock.tick()


            # obsługa ruchu, stałe wykonywanie niezalezne od fps
            if self.isRun:
                oneTick = (self.clock.tick() / 1000.0)
                if self.paused is False:
                    self.deltaTime += oneTick
                    self.snake.Move()
                elif self.paused is True:
                    self.screen.blit(pause, (625, 10))

            self.gui.draw()
            self.gameBoard.draw()
            self.food.draw()
            self.snake.draw()

            pygame.display.flip()

    def Defeat(self):
        # dźwięk obrażenia
        mixer.music.load("sounds/Getting hit.mp3")
        mixer.music.play()
        mixer.music.set_volume(2)
        run = True
        while run:
            self.screen = pygame.display.set_mode((1920, 1080))
            pygame.display.set_caption("Snake- Game Over")

            # kod który robi animowane tło
            self.win.fill((0, 0, 0))
            self.win.blit(self.bg, (self.i, 0))
            self.win.blit(self.bg, (self.width + self.i, 0))
            if self.i == -self.width:
                self.win.blit(self.bg, (self.width + self.i, 0))
                self.i = 0
            self.i -= 1
            self.screen.blit(self.GAME_OVER, (0, 0))

            czcionka = pygame.font.Font('customFont/NeueAachenProBold.TTF', 60)
            wynik = czcionka.render("Score: {0}".format(self.result), 1, (0, 0, 0))
            rekord = czcionka.render("Highscore: {0}".format(self.highscore), 1, (0, 0, 0))
            nowy_rekord = czcionka.render("New highscore!", 1, (255, 0, 0))
            self.screen.blit(wynik, (840, 480))
            if self.result < self.highscore:
                self.screen.blit(rekord, (780, 580))
            else:
                self.highscore = self.result
                with open(path.join(self.dir, HS_FILE), 'w') as f:
                    f.write(str(self.result))
                    #self.screen.blit(rekord, (780, 580))
                    self.screen.blit(nowy_rekord, (750, 580))


            self.retry_button = pygame.image.load("img/retry.png")
            self.exit_img = pygame.image.load("img/exit.png")
            self.retry_button = Buttonhover2.Button(700, 700, "img/retry", 0.7)
            self.exit_button = Buttonhover2.Button(700, 850, "img/exit", 0.7)
            self.retry_button.draw(self.screen)
            self.exit_button.draw(self.screen)

            if self.retry_button.tick():
                run = False
                game = Game(self.gameMode, self.gameBoard.width, self.gameBoard.height)
                game.Start()
                pass
            if self.exit_button.tick():
                sys.exit(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()