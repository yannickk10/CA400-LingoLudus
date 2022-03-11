import pygame
from settings import *
from score import Score
from display_target import Target

class HUD (pygame.sprite.Sprite):
    def __init__(self):
        super(HUD, self).__init__()
        self.image = pygame.image.load("Sprites/hud.png").convert()
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.rect.height

        #Add Score to hud
        self.score_object = Score()
        self.player_score = pygame.sprite.Group()
        self.player_score.add(self.score_object)

        # Add target name to hud
        self.target = Target()
        self.target_name = pygame.sprite.Group()
        self.target_name.add(self.target)


    def update(self):
        self.player_score.update()
