import pygame
import tools
from tools.Buttonhover2 import Button
from Game.direction import Direction
from pygame import mixer
import menu
import sys

class Gui():
    def __init__(self, game):
        self.game = game

        self.czcionka = pygame.font.Font('customFont/NeueAachenProBold.TTF', 60)
        self.background = pygame.image.load("img/tlo_game.jpg")
        self.exit_button = tools.Buttonhover2.Button(1410, 990, "img/exit", 0.6)
        self.on_button = tools.Buttonhover2.Button(1600, 40, "img/on", 1)
        self.off_button = tools.Buttonhover2.Button(1750, 40, "img/off", 1)

        self.dialogue_font = pygame.font.Font('customFont/upheavtt.ttf', 60)
        self.dialogue = self.dialogue_font.render("press 'SPACE BAR' to play", 1, (0, 0, 0))

    def draw(self):
        # rysowanie, wyświetlanie
        pygame.Surface.blit(self.game.screen, self.background, (0, 0))
        self.exit_button.draw(self.game.screen)
        self.on_button.draw(self.game.screen)
        self.off_button.draw(self.game.screen)

        # Przycisk exit
        if self.exit_button.tick():
            mixer.music.load("sounds/BG music - menu.mp3")
            mixer.music.play(-1)
            gameMenu = menu.menu()
            gameMenu.setSettings(self.game.gameMode, self.game.speedType, self.game.w, self.game.h, self.game.numberFruits)
            gameMenu.main_menu()
            sys.exit(0)

        # Opcje dźwięku
        if self.on_button.tick():
            mixer.music.set_volume(0.1)

        if self.off_button.tick():
            mixer.music.set_volume(0)

        wynik = self.czcionka.render("Score: {0}".format(self.game.result), 1, (0, 0, 0))

        if not self.game.isRun:
            self.game.screen.blit(self.dialogue, (540, 1000))

        self.game.screen.blit(wynik, (5, 10))