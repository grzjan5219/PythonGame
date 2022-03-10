import pygame
from Game.game import Game
from tools import button
from pygame import mixer
import Colours
from pyvidplayer import Video

# Kolor węża. Później tego nie będzie
kolor = Colours.red
class menu():
    def __init__(self):
        print("test")
        pygame.init()
        #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1920, 1080))
        # pygame.FULLSCREEN, pygame.RESIZABLE
        # na razie cofnąłem plik do wersji początkowej, bo z FULLSCREEN nie chciał poprawnie działać

        # nazwa okna
        pygame.display.set_caption("Snake")

        # tło
        self.tlo_img = pygame.image.load("img/tlo.jpg")
        # tło ustawień
        self.tlo_settings_img = pygame.image.load("img/tlo_settings.jpg")

        # muzyka w tle
        mixer.music.load("sounds/BG music - menu.mp3")
        mixer.music.play(-1)
        mixer.music.set_volume(0.1)

        # opcje wyboru
        self.start_img = pygame.image.load("img/start.png")
        self.settings_img = pygame.image.load("img/settings.png")
        self.exit_img = pygame.image.load("img/exit.png")
        self.on_img = pygame.image.load("img/on.png")
        self.off_img = pygame.image.load("img/off.png")
        self.back_img = pygame.image.load("img/back.png")

        self.start_button = button.Button(700, 450, self.start_img, 0.7)
        self.settings_button = button.Button(700, 600, self.settings_img, 0.7)
        self.exit_button = button.Button(700, 750, self.exit_img, 0.7)
        self.off_button = button.Button(1700, 950, self.off_img, 0.9)
        self.on_button = button.Button(1570, 950, self.on_img, 0.9)
        self.back_button = button.Button(700, 750, self.back_img, 0.7)

        self.vid = Video("video/tlo.mp4")
        self.vid.set_size((1920, 1080))

    # ustawienia wizualne (Tu będzie się znajdować zmiana kolorystyki węża, owocu i planszy)
    def wizualne(self):
        run = True
        while run:
            self.screen.blit(self.tlo_settings_img, (0, 0))
            pygame.display.set_caption("Snake- ustawienia")

            if self.exit_button.draw(self.screen):
                run = False
                print("exit")
                pass

            if self.back_button.draw(self.screen):
                print("exit")
                run = False
                pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()


    # główne ustawienia (Tu będą znajdować się opcje m.in. wizualne, zmiany  trudności..)
    def settings(self):
        run = True
        while run:
            self.screen.blit(self.tlo_settings_img, (0, 0))
            pygame.display.set_caption("Snake- ustawienia")

            # Zamiast przycisku start będzie przycisk "Ustawienia wizualne")
            if self.start_button.draw(self.screen):
                print("test")
                self.wizualne()
                pygame.display.update()

            if self.exit_button.draw(self.screen):
                run = False
                print("exit")
                pass

            if self.back_button.draw(self.screen):
                print("exit")
                run = False
                pass

            # opcje dźwięku
            if self.on_button.draw(self.screen):
                mixer.music.set_volume(0.1)
            if self.off_button.draw(self.screen):
                mixer.music.set_volume(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()



    def intro(self):
        while True:
            self.vid.draw(self.screen, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.vid.close()
                    self.main_menu()


    def main_menu(self):
        run = True
        while run:
            self.screen.blit(self.tlo_img, (0, 0))

            # start gry
            if self.start_button.draw(self.screen):
                game = Game()
                game.Start()
                print("start")
                pass

            #  przycisk ustawień w main menu
            if self.settings_button.draw(self.screen):
                self.settings()
                pygame.display.update()
                print("settings")

            # wyjście
            if self.exit_button.draw(self.screen):
                run = False
                print("exit")
                pass

            # opcje dźwięku
            if self.on_button.draw(self.screen):
                mixer.music.set_volume(0.1)
            if self.off_button.draw(self.screen):
                mixer.music.set_volume(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()
menu = menu()
#menu.main_menu()
menu.intro()
