import pygame
from settings import *
from button import *

class Pause_game(pygame.sprite.Sprite):
    def __init__(self):
        super(Pause_game, self).__init__()
        self.image = pygame.image.load("Sprites/pause_screen.png").convert()
        self.image.set_colorkey((10, 10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = P_SCREEN_WIDTH // 2 
        self.rect.y = P_SCREEN_HEIGHT - self.rect.height + 20

    def update(self):
        pass

