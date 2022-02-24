import pygame
import button

def menu():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))

    # nazwa okna
    pygame.display.set_caption("Snake")

    # tło
    tlo_img = pygame.image.load("tło.jpg")

    # opcje wyboru
    start_img = pygame.image.load("Przycisk START.png").convert_alpha()
    settings_img = pygame.image.load("Przycisk SETTINGS.png").convert_alpha()
    quit_img = pygame.image.load("Przycisk QUIT.png")

    start_button = button.Button(600, 400, start_img, 0.7)
    settings_button = button.Button(600, 600, settings_img, 0.7)
    quit_button = button.Button(600, 800, quit_img, 0.7)

    run = True
    while run:
        screen.blit(tlo_img, (0, 0))

        if start_button.draw(screen):
            print("start")
        if settings_button.draw(screen):
            print("settings")
        if quit_button.draw(screen):
            run = False
            print("quit")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()
menu()