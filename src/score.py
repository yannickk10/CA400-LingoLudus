import pygame
from settings import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.score = 0
        self.font = font = pygame.font.Font('freesansbold.ttf', 32)
        self.image = self.font.render("Score:" + str(self.score), False, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - self.rect.width - 30
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 30
