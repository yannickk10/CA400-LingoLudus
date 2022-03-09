import pygame
from settings import *
from score import Score

class HUD (pygame.sprite.Sprite):
    def __init__(self):
        super(HUD, self).__init__()
        self.image = pygame.image.load("Sprites/hud.png").convert()
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.rect.height

        #Add Score to health Bar
        self.score_object = Score()
        self.player_score = pygame.sprite.Group()
        self.player_score.add(self.score_object)

    def update(self):
        self.player_score.update()
