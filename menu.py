import pygame
import tools.button

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Menu ')

start_img = pygame.image.load('img/start.png').convert_alpha()
exit_img = pygame.image.load('img/exit.png').convert_alpha()

start_button = tools.button.Button(100, 200, start_img, 0.8)
exit_button = tools.button.Button(450, 200, exit_img, 0.8)

while True:

	screen.fill((202, 228, 241))

	if start_button.draw(screen):
		print('START')
	if exit_button.draw(screen):
		print('EXIT')

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	pygame.display.update()
