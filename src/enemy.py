import pygame
from settings import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite, backing_colour):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(sprite).convert()
        self.image.set_colorkey(backing_colour)
        self.start_pos_divider = 6
        self.rect, self.rect.x, self.rect.y = self.set_pos()
        self.speed = random.randint(6,7)

        #Enenmy status
        self.health = 1
        self.enemy_score = 0
        self.imposter_score = 100
        self.speed = random.randint(5,6)

    def update(self):
        self.rect.move_ip(-self.speed, 0)

    def set_pos(self):

        if self.start_pos_divider == 1:
            self.rect = self.image.get_rect()
            self.rect.y = SCREEN_HEIGHT / self.start_pos_divider
            self.rect.x = SCREEN_WIDTH
        else:
            self.rect = self.image.get_rect()
            self.rect.y = SCREEN_HEIGHT / self.start_pos_divider
            self.rect.x = SCREEN_WIDTH
        self.start_pos_divider -= 1
        print(self.start_pos_divider)
        
        return self.rect, self.rect.x, self.rect.y

    def get_hit(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
