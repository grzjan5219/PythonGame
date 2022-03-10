import pygame
import os

def animowane_tlo():
    win = pygame.display.set_mode((1920, 1080))
    bg_img = pygame.image.load(os.path.join("D:/git_project/PythonGame/img/tlo_wide.jpg"))
    bg = pygame.transform.scale(bg_img, (3840, 1080))

    width = 3840
    i = 0

    win.fill((0, 0, 0))

    run = True
    while run:
        # Create looping background
        win.blit(bg, (i, 0))
        win.blit(bg, (width + i, 0))
        if i == -width:
            win.blit(bg, (width + i, 0))
            i = 0
        i -= 1
        pygame.display.update()