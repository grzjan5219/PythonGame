import pygame
import sys

class Snake():
    def __init__(self):
        #inicjalizacja
        self.clock = pygame.time.Clock()
        pass

    def Start(self, screen):
        screen.fill((100, 200, 100))
        snake = pygame.Rect(200, 200, 30, 30)

        while True:
            # obługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            # obsługa wejścia
            keysPressed = pygame.key.get_pressed()
            if(keysPressed[pygame.K_d]):
                snake.x += 1
            if(keysPressed[pygame.K_a]):
                snake.x -= 1
            if (keysPressed[pygame.K_w]):
                snake.y -= 1
            if (keysPressed[pygame.K_s]):
                snake.y += 1

            # rysowanie, wyświetlanie
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255 , 0, 0), snake)
            pygame.display.flip()