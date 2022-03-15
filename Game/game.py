from Game.snake import Snake
from Game.board import Board
import pygame
import sys
from pygame import mixer
from Game.food import Food
from Game.przeszkoda import Przeszkoda
from Game.direction import Direction
from Game.fruitType import FruitType
from Game.gameMode import GameMode
from tools import Buttonhover2
from Game.przeszkodaType import PrzeszkodaType
from os import path

#plik który przechowuje najwyższy wynik
HS_FILE = "highscore.txt"

class Game():
    def __init__(self):
        #inicjalizacja
        self.clock = pygame.time.Clock()
        self.speed = 4
        self.tps = 100.0
        self.deltaTime = 0.0
        self.paused = False
        self.isRun = False
        self.result = 0
        # 1200 # 880

        big_map = 20
        medium_map = 15
        small_map = 10

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.screen = pygame.display.set_mode((1000, 800))
        self.gameBoard = Board(medium_map, medium_map, self) # width  - max 60 (min - 5)  height - max 44 (min - 5)
                                             # sizeBlock - minimum 20
        #print(self.screen.get_width(), self.screen.get_height())
        # tryb gry
        self.gameMode = GameMode.timeWarp

        self.snake = Snake(self)
        self.food = Food(self)
        self.przeszkoda = Przeszkoda(self)
        # trzy owoce
        self.food.add(FruitType.common)
        self.food.add(FruitType.common)
        self.food.add(FruitType.common)
        self.przeszkoda.add(PrzeszkodaType.common)
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
        czcionka = pygame.font.Font('customFont/NeueAachenProBold.TTF', 60)
        background = pygame.image.load("img/tlo_game.jpg")
        exit_button= Buttonhover2.Button(1400, 950, "img/exit", 0.7)
        on_button = Buttonhover2.Button(1600, 40, "img/on", 1)
        off_button = Buttonhover2.Button(1750, 40, "img/off", 1)

        run = True
        while run:
            # rysowanie, wyświetlanie
            pygame.Surface.blit(self.screen, background, (0, 0))
            exit_button.draw(self.screen)
            on_button.draw(self.screen)
            off_button.draw(self.screen)

            # Przycisk exit
            if exit_button.tick():
                mixer.music.load("sounds/BG music - menu.mp3")
                mixer.music.play(-1)
                return True

            # Opcje dźwięku
            if on_button.tick():
                mixer.music.set_volume(0.1)

            if off_button.tick():
                mixer.music.set_volume(0)

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
                            print("Start")
                            self.food.spawn()
                            self.przeszkoda.spawn()
                            self.snake.turningDirection = Direction.none
                            self.isRun = True
                            self.clock.tick()


            # obsługa ruchu, stałe wykonywanie niezalezne od fps
            if self.isRun  and self.paused is False:
                self.deltaTime += (self.clock.tick() / 1000.0)
                self.snake.Move()

            self.gameBoard.draw()
            # tymczasowy prostokąt wyznaczający miejsce na informację
            #pygame.draw.rect(self.screen, (0 , 255, 0), pygame.Rect(1100, 80, 360, 700))
            #pygame.draw.rect(self.screen, (0 , 255, 0), pygame.Rect(100, 100, 1200, 880))
            self.food.draw()
            self.snake.draw()
            self.przeszkoda.draw()

            global wynik
            wynik = czcionka.render("Score: {0}".format(self.result), 1, (0, 0, 0))

            dialogue_font = pygame.font.Font('customFont/upheavtt.ttf', 60)
            dialogue = dialogue_font.render("press 'SPACE BAR' to play", 1, (0, 0, 0))
            self.screen.blit(dialogue, (325, 1000))
            self.screen.blit(wynik, (5, 10))

            pygame.display.flip()

    def Defeat(self):
        #print("Przegrana punkty: ", self.result)
        #self.isRun = False
        #sys.exit(0)

        # dźwięk obrażenia
        mixer.music.load("sounds/Getting hit.mp3")
        mixer.music.play()
        mixer.music.set_volume(2)
        run = True
        while run:
            self.screen = pygame.display.set_mode((1920, 1080))
            pygame.display.set_caption("Snake- Game Over")
            self.tlo_game_over_img = pygame.image.load("img/tlo_game_over.jpg")

            self.screen.blit(self.tlo_game_over_img, (0, 0))
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
                print("start")
                run = False
                game = Game()
                game.Start()
                pass
            if self.exit_button.tick():
                sys.exit(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()