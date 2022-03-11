import pygame
from Game.game import Game
from tools import Buttonhover2
from tools import button
from pygame import mixer

class menu():
    def __init__(self):
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
        self.on_img = pygame.image.load("img/on.png")
        self.off_img = pygame.image.load("img/off.png")

        self.start_button = Buttonhover2.Button(600, 450, "img/start")
        self.settings_button = Buttonhover2.Button(600, 620, "img/settings")
        self.exit_button = Buttonhover2.Button(600, 790, "img/exit")
        self.off_button = button.Button(1700, 950, self.off_img, 0.9)
        self.on_button = button.Button(1570, 950, self.on_img, 0.9)
        self.back_button = Buttonhover2.Button(600, 750, "img/back")

    # ustawienia wizualne (Tu będzie się znajdować zmiana kolorystyki węża, owocu i planszy)
    def wizualne(self):
        run = True
        while run:
            self.screen.blit(self.tlo_settings_img, (0, 0))
            pygame.display.set_caption("Snake- ustawienia")
            self.exit_button.draw(self.screen)
            self.back_button.draw(self.screen)

            if self.exit_button.tick():
                run = False
                print("exit")
                pass

            if self.back_button.tick():
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
        run2 = True
        while run2:
            self.screen.blit(self.tlo_settings_img, (0, 0))
            self.start_button.draw(self.screen)
            self.back_button.draw(self.screen)
            pygame.display.set_caption("Snake- ustawienia")

            # Zamiast przycisku start będzie przycisk "Ustawienia wizualne")
            if self.start_button.tick():
                print("test")
                self.wizualne()
                pygame.display.update()

            if self.back_button.tick():
                return True

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

    def main_menu(self):
        run = True
        while run:
            self.screen.blit(self.tlo_img, (0, 0))
            self.start_button.draw(self.screen)
            self.settings_button.draw(self.screen)
            self.exit_button.draw(self.screen)

            # start gry
            if self.start_button.tick():
                game = Game()
                game.Start()
                print("start")
                pass

            #  przycisk ustawień w main menu
            if self.settings_button.tick():
                self.settings()
                pygame.display.update()
                print("settings")

            # wyjście
            if self.exit_button.tick():
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
menu.main_menu()
