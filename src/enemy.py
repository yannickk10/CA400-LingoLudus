import pygame
from settings import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite, backing_colour):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(sprite).convert_alpha()
        self.image.set_colorkey(backing_colour)
        self.rect = self.image.get_rect(center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 200),
                random.randint(60, SCREEN_HEIGHT- 120),))

        self.speed = random.randint(6,7)

        #Enenmy status
        self.health = 1
        self.enemy_score = 0
        self.imposter_score = 100
        self.speed = random.randint(5,7)

    def update(self):
        self.rect.move_ip(-self.speed, 0)

    def get_hit(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
