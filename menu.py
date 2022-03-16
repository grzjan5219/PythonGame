import pygame
from Game.game import Game
from Game.gameMode import GameMode
from tools import Buttonhover2
from pygame import mixer
from tools.pyvidplayer import Video
from tools.button import Button

class menu():
    def __init__(self):
        pygame.init()
        self.setDefaultSettings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.MAXWIDTH = 60
        self.MAXHEIGHT = 44
        self.MINWIDTH = 5
        self.MINHEIGHT = 5

        self.dialogue_font = pygame.font.Font('customFont/NeueAachenProBold.TTF', 60)
        self.dialogue = self.dialogue_font.render("Penetrating through walls: ", 1, (0, 0, 0))
        self.speedDialogue = self.dialogue_font.render("Speed: ", 1, (0, 0, 0))

        self.mapSizeWidthDialoque = self.dialogue_font.render(f"Map size(width):    {self.mapSizeWidth}", 1, (0, 0, 0))
        self.mapSizeHeightDialoque = self.dialogue_font.render(f"Map size(height):   {self.mapSizeHeight}", 1, (0, 0, 0))

        self.plusWidth = Button(1200, 650, pygame.image.load("img/plus.png"), 0.1)
        self.minusWidth = Button(1300, 665, pygame.image.load("img/minus.png"), 0.1)

        self.plusHeight = Button(1200, 750, pygame.image.load("img/plus.png"), 0.1)
        self.minusHeight = Button(1300, 765, pygame.image.load("img/minus.png"), 0.1)

        pygame.display.set_caption("Snake")

        self.tlo_img = pygame.image.load("img/tlo.jpg")
        self.tlo_settings_img = pygame.image.load("img/tlo_settings.jpg")

        # opcje wyboru
        self.on_img = pygame.image.load("img/on.png")
        self.off_img = pygame.image.load("img/off.png")

        self.start_button = Buttonhover2.Button(650, 450, "img/start", 0.8)
        self.settings_button = Buttonhover2.Button(650, 620, "img/settings", 0.8)
        self.exit_button = Buttonhover2.Button(650, 790, "img/exit", 0.8)
        self.back_button = Buttonhover2.Button(650, 920, "img/back", 0.8)
        self.on_button = Buttonhover2.Button(1550, 950, "img/on", 1)
        self.off_button = Buttonhover2.Button(1700, 950, "img/off", 1)
        self.on2_button = Buttonhover2.Button(1150, 450, "img/on", 1)
        self.off2_button = Buttonhover2.Button(1300, 450, "img/off", 1)

        self.onHoverButton = Button(1150, 450, pygame.image.load("img/onhover.png"), 1)
        self.offHoverButton = Button(1300, 450,  pygame.image.load("img/offhover.png"), 1)

        # filmik, który pokazuje się przed samą grą
        self.vid = Video("video/intro.mp4")
        self.vid.set_size((1920, 1080))

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

            self.screen.blit(self.dialogue, (450, 450))
            self.screen.blit(self.speedDialogue, (450, 550))
            self.screen.blit(self.mapSizeWidthDialoque, (450, 650))
            self.screen.blit(self.mapSizeHeightDialoque, (450, 750))

            self.back_button.draw(self.screen)
            self.on_button.draw(self.screen)
            self.off_button.draw(self.screen)

            if self.gameMode == GameMode.standard:
                self.offHoverButton.draw(self.screen)
                self.on2_button.draw(self.screen)
            elif self.gameMode == GameMode.timeWarp:
                self.onHoverButton.draw(self.screen)
                self.off2_button.draw(self.screen)

            pygame.display.set_caption("Snake - ustawienia")

            if self.plusWidth.draw(self.screen):
                if self.mapSizeWidth < self.MAXWIDTH:
                   self.mapSizeWidth += 1
                   self.mapSizeWidthDialoque = self.dialogue_font.render(f"Map size(width):    {self.mapSizeWidth}", 1,(0, 0, 0))

            if self.minusWidth.draw(self.screen):
                if self.mapSizeWidth > self.MINWIDTH:
                    self.mapSizeWidth -= 1
                    self.mapSizeWidthDialoque = self.dialogue_font.render(f"Map size(width):    {self.mapSizeWidth}", 1,(0, 0, 0))

            if self.plusHeight.draw(self.screen):
                if self.mapSizeHeight < self.MAXHEIGHT:
                    self.mapSizeHeight += 1
                    self.mapSizeHeightDialoque = self.dialogue_font.render(f"Map size(height):   {self.mapSizeHeight}", 1, (0, 0, 0))

            if self.minusHeight.draw(self.screen):
                if self.mapSizeHeight > self.MINHEIGHT:
                    self.mapSizeHeight -= 1
                    self.mapSizeHeightDialoque = self.dialogue_font.render(f"Map size(height):   {self.mapSizeHeight}", 1, (0, 0, 0))

            # Zamiast przycisku start będzie przycisk "Ustawienia wizualne")
            if self.on2_button.tick():
                self.gameMode = GameMode.timeWarp
                #print(self.gameMode)

            if self.off2_button.tick():
                self.gameMode = GameMode.standard
                #print(self.gameMode)

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

    def setDefaultSettings(self):
        self.gameMode = GameMode.standard
        self.mapSizeWidth = 15
        self.mapSizeHeight = 15

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
                game = Game(self.gameMode, self.mapSizeWidth, self.mapSizeHeight)
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
