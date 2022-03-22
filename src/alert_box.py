import pygame
from settings import * 

class AlertBox(pygame.sprite.Sprite):
    def __init__(self, text):
        super(AlertBox, self).__init__()
        self.font = pygame.font.Font("assets/font.ttf", 50)
        self.colour = ("red")
        self.text = text
        self.image = self.font.render(self.text, False, self.colour)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2
        self.rect.y = SCREEN_HEIGHT // 2 - self.rect.height // 2

    def update(self):
        pass