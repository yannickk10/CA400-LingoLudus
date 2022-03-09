import pygame
from settings import *

class HUD (pygame.sprite.Sprite):
    def __init__(self):
        super(HUD, self).__init__()
        self.image = pygame.image.load("Sprites/hud.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.rect.height

    def update(self):
        pass
