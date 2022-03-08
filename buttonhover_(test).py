#test.py
import pygame
import sys
from pygame import mixer



pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Button!")

button_surface = pygame.image.load("D:\git_project\PythonGame\img\start.png")


class Button():
	def __init__(self, image, x_pos, y_pos):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.image = pygame.image.load("D:\git_project\PythonGame\img\starthover.png")
		else:
			# muzyka
			mixer.music.load("D:\git_project\PythonGame\sounds\Menu selection.mp3")
			mixer.music.play(0)
			mixer.music.set_volume(1)
			self.image = pygame.image.load("D:\git_project\PythonGame\img\start.png")


button = Button(button_surface, 400, 300)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())

	screen.fill("red")

	button.update()
	button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()