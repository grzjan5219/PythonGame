import pygame
import sys

class Snake():
    def __init__(self):
        #inicjalizacja
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.deltaTime = 0
        self.snake = pygame.Rect(200, 200, 30, 30)

    def Start(self, screen):
        screen.fill((100, 200, 100))
        currentKey = 'q'

        while True:
            # obługa zdarzeń
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_w:
                        currentKey = "w"
                    if event.key == pygame.K_s:
                        currentKey = "s"
                    if event.key == pygame.K_a:
                        currentKey = "a"
                    if event.key == pygame.K_d:
                        currentKey = "d"

            # obsługa ruchu
            self.deltaTime += self.clock.tick() / 1000.0
            self.Move(currentKey, 5)

            # rysowanie, wyświetlanie
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, (255 , 0, 0), self.snake)
            pygame.display.flip()


    def Move(self, key, speed):

        while self.deltaTime > (1 / self.fps):

            if key == "q":
                return

            if key == "w":
                self.snake.y -= speed
            if key == "s":
                self.snake.y += speed
            if key == "a":
                self.snake.x -= speed
            if key == "d":
                self.snake.x += speed

            self.deltaTime -= (1 / self.fps)
