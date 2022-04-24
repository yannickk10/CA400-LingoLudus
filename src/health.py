import pygame
from settings import *

class Health(pygame.sprite.Sprite):
    def __init__(self):
        super(Health, self).__init__()
        self.image = pygame.image.load("assets/Sprites/full_health.png").convert()
        self.rect = self.image.get_rect()

    def update(self, player_health):
        if player_health == 4:
            self.image = pygame.image.load("assets/Sprites/full_health.png").convert()
            self.rect = self.image.get_rect()
            self.rect.x = 20
            self.rect.y = SCREEN_HEIGHT - self.rect.height * 2
        elif player_health == 3:
            self.image = pygame.image.load("assets/Sprites/tq_health.png").convert()
            self.rect = self.image.get_rect()
            self.rect.x = 20
            self.rect.y = SCREEN_HEIGHT - self.rect.height * 2
        elif player_health == 2:
            self.image = pygame.image.load("assets/Sprites/oe_health.png").convert()
            self.rect = self.image.get_rect()
            self.rect.x = 20
            self.rect.y = SCREEN_HEIGHT - self.rect.height * 2
        elif player_health == 1:
            self.image = pygame.image.load("assets/Sprites/lowest_health.png").convert()
            self.rect = self.image.get_rect()
            self.rect.x = 20
            self.rect.y = SCREEN_HEIGHT - self.rect.height * 2
        elif player_health == 0:
            self.image = pygame.image.load("assets/Sprites/no_health.png").convert()
            self.rect = self.image.get_rect()
            self.rect.x = 20
            self.rect.y = SCREEN_HEIGHT - self.rect.height * 2
