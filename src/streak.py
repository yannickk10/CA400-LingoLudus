import pygame
from settings import *

class Streak(pygame.sprite.Sprite):
    def __init__(self):
        super(Streak, self).__init__()
        self.streak = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.image = self.font.render("Streak:" + str(self.streak), False, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - self.rect.width - 30
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 55

    def update(self):
        pass

    def update_streak(self):
        self.streak += 1
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.image = self.font.render("Streak:" + str(self.streak), False, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - self.rect.width - 30
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 55

    def reset_streak(self):
        self.streak = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.image = self.font.render("Streak:" + str(self.streak), False, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - self.rect.width - 30
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 55