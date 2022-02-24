import pygame
import sys

pygame.init()

background = (0, 0, 0)
snake = (0, 0, 255)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake")

game_over = False

x1 = 400
y1 = 300

clock = pygame.time.Clock()

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True

  screen.fill(background)
  pygame.draw.rect(screen, snake, [x1, y1, 10, 10])

  pygame.display.update()


pygame.quit()
quit()