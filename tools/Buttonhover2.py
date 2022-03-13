import pygame

class Button:
    def __init__(self, x_cord, y_cord, file_name, scale):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.button_image = pygame.image.load(f"{file_name}.png")
        self.hovered_button_image = pygame.image.load(f"{file_name}hover.png")
        width = self.button_image.get_width()
        height = self.button_image.get_height()
        width_hover = self.hovered_button_image.get_width()
        height_hover = self.hovered_button_image.get_height()
        self.button_image = pygame.transform.scale(self.button_image, (int(width * scale), int(height * scale)))
        self.hovered_button_image = pygame.transform.scale(self.hovered_button_image, (int(width_hover * scale), int(height_hover * scale)))
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_image.get_width(), self.button_image.get_height())

    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw(self, window):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.hovered_button_image, (self.x_cord, self.y_cord))
        else:
            window.blit(self.button_image, (self.x_cord, self.y_cord))