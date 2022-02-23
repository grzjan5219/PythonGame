<<<<<<< HEAD
import pygame
import sys

=======
<<<<<<< HEAD

=======
import pygame
import sys

>>>>>>> a6feeb0 (Wyskakiwanie okienka)
pygame.init()

pygame.display.set_caption("Snake")

screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
<<<<<<< HEAD
=======
>>>>>>> 0f3a5c3 (Wyskakiwanie okienka)
>>>>>>> a6feeb0 (Wyskakiwanie okienka)
