import pygame
from Game.game import Game
from tools import button
from pygame import mixer

def menu():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    #, pygame.FULLSCREEN, pygame.RESIZABLE
    # na razie cofnąłem plik do wersji początkowej, bo z FULLSCREEN nie chciał poprawnie działać

    # nazwa okna
    pygame.display.set_caption("Snake")

    # tło
    tlo_img = pygame.image.load("img/tlo.jpg").convert_alpha()

    #muzyka w tle
    mixer.music.load("sounds/BG music - menu.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)


    # opcje wyboru
    start_img = pygame.image.load("img/start.png").convert_alpha()
    settings_img = pygame.image.load("img/settings.png").convert_alpha()
    exit_img = pygame.image.load("img/exit.png").convert_alpha()

    start_button = button.Button(600, 450, start_img, 0.7)
    settings_button = button.Button(600, 600, settings_img, 0.7)
    exit_button = button.Button(600, 750, exit_img, 0.7)

    run = True
    while run:
        screen.blit(tlo_img, (0, 0))

        if start_button.draw(screen):
            game = Game()
            game.Start()
            print("start")
            pass
        if settings_button.draw(screen):
            print("settings")
        if exit_button.draw(screen):
            run = False
            print("exit")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
menu()