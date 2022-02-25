import pygame
import sys
from pygame import mixer

pygame.init()

#muzyka w tle
mixer.music.load("sounds/BG music - game.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.1)

background = (0, 0, 0)
snake = (0, 0, 255)

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

game_over = False

x1 = 400
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        x1_change = -10
        y1_change = 0
      elif event.key == pygame.K_RIGHT:
        x1_change = 10
        y1_change = 0
      elif event.key == pygame.K_UP:
        x1_change = 0
        y1_change = -10
      elif event.key == pygame.K_DOWN:
        x1_change = 0
        y1_change = 10

  if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
    game_over = True

  x1 += x1_change
  y1 += y1_change

  screen.fill(background)
  pygame.draw.rect(screen, snake, [x1, y1, 10, 10])

  pygame.display.update()

  clock.tick(30)

pygame.quit()
quit()