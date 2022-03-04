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
        # 1200 # 880

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.gameBoard = Board(15, 15, self) # width  - max 60 (min - 5)  height - max 44 (min - 5)
                                             # sizeBlock - minimum 20
        #print(self.screen.get_width(), self.screen.get_height())

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
        czcionka = pygame.font.SysFont('comicsans', 40)
        background = pygame.image.load("img/tlo_game.jpg")
        exit_img = pygame.image.load("img/exit.png")
        on_img = pygame.image.load("img/on.png")
        off_img = pygame.image.load("img/off.png")

        off_button = button.Button(1750, 40, off_img, 0.9)
        on_button = button.Button(1620, 40, on_img, 0.9)
        exit_button = button.Button(1500, 950, exit_img, 0.5)

        while True:
            # rysowanie, wyświetlanie
            pygame.Surface.blit(self.screen, background, (0, 0))

            # Przycisk exit
            if exit_button.draw(self.screen):
                mixer.music.load("sounds/BG music - menu.mp3")
                mixer.music.play(-1)
                return True

            # Opcje dźwięku
            if on_button.draw(self.screen):
                mixer.music.set_volume(0.1)

            if off_button.draw(self.screen):
                mixer.music.set_volume(0)

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
            #pygame.draw.rect(self.screen, (0 , 255, 0), pygame.Rect(1100, 80, 360, 700))
            #pygame.draw.rect(self.screen, (0 , 255, 0), pygame.Rect(100, 100, 1200, 880))
            self.food.draw()
            self.snake.draw()

            global wynik
            wynik = czcionka.render("Punkty: {0}".format(self.result), 1, (255, 255, 0))

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
            czcionka = pygame.font.SysFont('comicsans', 100)
            wynik = czcionka.render("Punkty: {0}".format(self.result), 1, (0, 0, 0))
            self.screen.blit(wynik, (720, 500))

            self.start_img = pygame.image.load("img/start.png")
            self.exit_img = pygame.image.load("img/exit.png")
            self.start_button = button.Button(700, 700, self.start_img, 0.7)
            self.exit_button = button.Button(700, 850, self.exit_img, 0.7)

            if self.start_button.draw(self.screen):
                game = Game()
                game.Start()
                print("start")
                pass
            if self.exit_button.draw(self.screen):
                sys.exit(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()