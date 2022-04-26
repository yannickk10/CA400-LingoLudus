import pygame
from settings import *
from score import Score
from streak import Streak
from display_target import Target
from health import Health

class HUD (pygame.sprite.Sprite):
    def __init__(self):
        super(HUD, self).__init__()

        #Create initial hud image
        self.initial_image = pygame.image.load("assets/Sprites/hud.png").convert()
        self.initial_image_rect = self.initial_image.get_rect()



        #Transform it to match the screen size 
        self.image = pygame.transform.scale(self.initial_image, (SCREEN_WIDTH,self.initial_image_rect.height))
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.rect.height

        # Add Score to hud
        self.score_object = Score()
        self.player_score = pygame.sprite.Group()
        self.player_score.add(self.score_object)

        # Add Streak to hud
        self.streak_object = Streak()
        self.player_streak = pygame.sprite.Group()
        self.player_streak.add(self.streak_object)

        # Add target name to hud
        self.target = Target()
        self.target_name = pygame.sprite.Group()
        self.target_name.add(self.target)

        # Add target Health to hud
        self.health = Health()
        self.health_bar = pygame.sprite.Group()
        self.health_bar.add(self.health)


    def update(self):
        self.player_score.update()
