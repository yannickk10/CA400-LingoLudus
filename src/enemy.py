import pygame
from settings import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite, backing_colour):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(sprite).convert_alpha()
        self.image.set_colorkey(backing_colour, pygame.RLEACCEL)
        self.rect = self.image.get_rect(center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(10, SCREEN_HEIGHT- 120),))

        self.speed = random.randint(5,6)

        #Enenmy status
        self.health = 1
        self.enemy_score = 50
        self.speed = random.randint(5,6)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
