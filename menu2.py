import pygame
from tools import button


def menu():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))

    # nazwa okna
    pygame.display.set_caption("Snake")

    # tło
    tlo_img = pygame.image.load("img/tlo.jpg").convert_alpha()

    # opcje wyboru
    start_img = pygame.image.load("img/start.png").convert_alpha()
    settings_img = pygame.image.load("img/settings.png").convert_alpha()
    exit_img = pygame.image.load("img/exit.png").convert_alpha()

    start_button = button.Button(600, 400, start_img, 0.7)
    settings_button = button.Button(600, 600, settings_img, 0.7)
    exit_button = button.Button(600, 800, exit_img, 0.7)

    run = True
    while run:
        screen.blit(tlo_img, (0, 0))

        if start_button.draw(screen):
            print("start")
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