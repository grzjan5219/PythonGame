import pygame
from Game.game import Game
from tools import button
from pygame import mixer
import Colours

kolor = Colours.red
def menu():
    pygame.init()
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1920, 1080))
    #, pygame.FULLSCREEN, pygame.RESIZABLE
    # na razie cofnąłem plik do wersji początkowej, bo z FULLSCREEN nie chciał poprawnie działać

    # nazwa okna
    pygame.display.set_caption("Snake")

    # tło
    tlo_img = pygame.image.load("img/tlo.jpg")
    # tło ustawień
    tlo_settings_img = pygame.image.load("img/tlo_settings.jpg")

    #muzyka w tle
    mixer.music.load("sounds/BG music - menu.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)

    # opcje wyboru
    start_img = pygame.image.load("img/start.png")
    settings_img = pygame.image.load("img/settings.png")
    exit_img = pygame.image.load("img/exit.png")
    on_img = pygame.image.load("img/on.png")
    off_img = pygame.image.load("img/off.png")
    back_img = pygame.image.load("img/back.png")

    start_button = button.Button(700, 450, start_img, 0.7)
    settings_button = button.Button(700, 600, settings_img, 0.7)
    exit_button = button.Button(700, 750, exit_img, 0.7)
    off_button = button.Button(1700, 950, off_img, 0.9)
    on_button = button.Button(1570, 950, on_img, 0.9)
    back_button = button.Button(700, 750, back_img, 0.7)

    # ustawienia
    def settings():
        run = True
        while run:
            screen.blit(tlo_settings_img, (0, 0))
            pygame.display.set_caption("Snake- ustawienia")

            if start_button.draw(screen):
                print("test")
                kolor = Colour.black
                pygame.display.update()

            if exit_button.draw(screen):
                run = False
                print("exit")
                pass

            if back_button.draw(screen):
                print("exit")
                run = False
                pass

            # opcje dźwięku
            if on_button.draw(screen):
                mixer.music.set_volume(0.1)
            if off_button.draw(screen):
                mixer.music.set_volume(0)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.display.update()

    # main menu
    run = True
    while run:
        screen.blit(tlo_img, (0, 0))

        # start gry
        if start_button.draw(screen):
            game = Game()
            game.Start()
            print("start")
            pass

        #  przycisk ustawień w main menu
        if settings_button.draw(screen):
            settings()
            pygame.display.update()
            print("settings")

        #wyjście
        if exit_button.draw(screen):
            run = False
            print("exit")
            pass

        #opcje dźwięku
        if on_button.draw(screen):
            mixer.music.set_volume(0.1)
        if off_button.draw(screen):
            mixer.music.set_volume(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
menu()