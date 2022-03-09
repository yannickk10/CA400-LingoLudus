import pygame
from settings import *
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):

    #Create the player image
        super(Player, self).__init__()
        self.image = pygame.image.load("Sprites/jet.png").convert()
        self.image.set_colorkey((255,255,255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()

        #creating the bullet group for the ships bullets
        self.bullets = pygame.sprite.Group()
        self.shoot_cooldown = 0
