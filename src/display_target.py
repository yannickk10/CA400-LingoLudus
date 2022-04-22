import pygame
from settings import *

class Target(pygame.sprite.Sprite):
    def __init__(self):
        super(Target, self).__init__()
        self.target = ""
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.image = self.font.render("Target:" + self.target, False, "Orange")
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2 - self.rect.width + 20
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 30


    def update(self, new_target):
        if new_target != None:
            self.target = new_target
            self.font = pygame.font.Font('freesansbold.ttf', 32)
            self.image = self.font.render("Target: " + str(self.target), False, "Orange")
            self.rect = self.image.get_rect()
            self.rect.x = SCREEN_WIDTH / 2 - self.rect.width + 20
            self.rect.y = SCREEN_HEIGHT - self.rect.height - 30
