import pygame
from Game.game import Game
from Game.gameMode import GameMode
from tools import Buttonhover2
from pygame import mixer
from tools.pyvidplayer import Video

class menu():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption("Snake")

        self.tlo_img = pygame.image.load("img/tlo.jpg")
        self.tlo_settings_img = pygame.image.load("img/tlo_settings.jpg")

        # opcje wyboru
        self.on_img = pygame.image.load("img/on.png")
        self.off_img = pygame.image.load("img/off.png")

        self.start_button = Buttonhover2.Button(650, 450, "img/start", 0.8)
        self.settings_button = Buttonhover2.Button(650, 620, "img/settings", 0.8)
        self.exit_button = Buttonhover2.Button(650, 790, "img/exit", 0.8)
        self.back_button = Buttonhover2.Button(650, 750, "img/back", 0.8)
        self.on_button = Buttonhover2.Button(1550, 950, "img/on", 1)
        self.off_button = Buttonhover2.Button(1700, 950, "img/off", 1)
        self.on2_button = Buttonhover2.Button(1150, 540, "img/on", 1)
        self.off2_button = Buttonhover2.Button(1300, 540, "img/off", 1)

        # filmik, który pokazuje się przed samą grą
        self.vid = Video("video/intro.mp4")
        self.vid.set_size((1920, 1080))

        self.gameMode = GameMode.standard

        # muzyka w tle
        mixer.music.load("sounds/BG music - menu.mp3")
        mixer.music.play(-1)
        mixer.music.set_volume(0.1)

    # ustawienia wizualne (Tu będzie się znajdować zmiana kolorystyki węża, owocu i planszy)
    def wizualne(self):
        while True:
            self.screen.blit(self.tlo_settings_img, (0, 0))
            pygame.display.set_caption("Snake - ustawienia")
            self.exit_button.draw(self.screen)
            self.back_button.draw(self.screen)

            if self.back_button.tick():
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()


    # główne ustawienia (Tu będą znajdować się opcje m.in. wizualne, zmiany  trudności..)
    def settings(self):
        while True:
            self.screen.blit(self.tlo_settings_img, (0, 0))
            self.dialogue_font = pygame.font.Font('customFont/NeueAachenProBold.TTF', 60)
            self.dialogue = self.dialogue_font.render("Penetrating through walls: ", 1, (0, 0, 0))
            self.screen.blit(self.dialogue, (450, 540))
            self.back_button.draw(self.screen)
            self.on_button.draw(self.screen)
            self.off_button.draw(self.screen)
            self.on2_button.draw(self.screen)
            self.off2_button.draw(self.screen)

            pygame.display.set_caption("Snake - ustawienia")

            # Zamiast przycisku start będzie przycisk "Ustawienia wizualne")
            if self.on2_button.tick():
                self.gameMode = GameMode.timeWarp
                print(self.gameMode)
                return

            if self.off2_button.tick():
                self.gameMode = GameMode.standard
                print(self.gameMode)
                return

            if self.back_button.tick():
                print("back")
                return True

                # opcje dźwięku
            if self.on_button.tick():
                mixer.music.set_volume(0.1)
            if self.off_button.tick():
                mixer.music.set_volume(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()


    # załadowanie intra
    def intro(self):
        while True:
            mixer.music.pause()
            self.vid.draw(self.screen, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.QUIT:
                    self.vid.close()
                    mixer.music.unpause()
                    self.main_menu()
                    pygame.quit()
                    quit()


    def main_menu(self):
        while True:
            self.screen.blit(self.tlo_img, (0, 0))
            self.start_button.draw(self.screen)
            self.settings_button.draw(self.screen)
            self.exit_button.draw(self.screen)
            self.on_button.draw(self.screen)
            self.off_button.draw(self.screen)

            # start gry
            if self.start_button.tick():
                game = Game(self.gameMode)
                game.Start()

            #  przycisk ustawień w main menu
            if self.settings_button.tick():
                self.settings()
                pygame.display.update()

            # wyjście
            if self.exit_button.tick():
                break

            # opcje dźwięku
            if self.on_button.tick():
                mixer.music.set_volume(0.1)
            if self.off_button.tick():
                mixer.music.set_volume(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()

menu = menu()
menu.intro()
