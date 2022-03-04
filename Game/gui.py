import pygame
from tools.button import Button
from Game.direction import Direction
from pygame import mixer

class Gui():
    def __init__(self, game):
        self.game = game

        #czcionka = pygame.font.SysFont('comicsans', 40)

        exit_img = pygame.image.load("img/exit.png")
        on_img = pygame.image.load("img/on.png")
        off_img = pygame.image.load("img/off.png")

        self.off_button = Button(1610, 760, off_img, 0.9)
        self.on_button = Button(1480, 760, on_img, 0.9)
        self.exit_button = Button(1435, 880, exit_img, 0.5)
        self.dialogue_font = pygame.font.Font('customFont/upheavtt.ttf', 60)

        self.dialogue = self.dialogue_font.render("press 'SPACE BAR' to play", 1, (0, 0, 0))

    def draw(self):
        # Przycisk exit
        if self.exit_button.draw(self.game.screen):
            mixer.music.load("sounds/BG music - menu.mp3")
            mixer.music.play(-1)
            return True

        # Opcje dźwięku
        if self.on_button.draw(self.game.screen):
            mixer.music.set_volume(0.1)

        if self.off_button.draw(self.game.screen):
            mixer.music.set_volume(0)

        result = self.dialogue_font.render("Punkty {0}".format(self.game.result), 1, (0, 0, 0))

        self.game.screen.blit(result, (1450, 150))

        if not self.game.isRun:
            self.game.screen.blit(self.dialogue, (300, 700))
