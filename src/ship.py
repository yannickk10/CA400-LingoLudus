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

    def update(self, pressed_keys):
        #update the players movements based on inputs

        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(10, 0)
