import pygame
import sys
import tools.button
import Games.Snake

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Menu ')

start_img = pygame.image.load('img/start.png').convert_alpha()
exit_img = pygame.image.load('img/exit.png').convert_alpha()
settings_img = pygame.image.load('img/settings.jpg').convert_alpha()

start_button = tools.button.Button(100, 200, start_img, 0.8)
exit_button = tools.button.Button(450, 200, exit_img, 0.8)
settings_button = tools.button.Button(100, 400, settings_img, 0.8)

screen.fill((200, 200, 250))

while True:
	if start_button.draw(screen):
		snake = Games.Snake.Snake()
		snake.Start(screen)
		print('START')
	if exit_button.draw(screen):
		print('EXIT')
	if settings_button.draw(screen):
		print('SETTINGS')

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)

	pygame.display.update()
