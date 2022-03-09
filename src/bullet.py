import pygame
from settings import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self):

        #create the bullet image
        super(Bullet, self).__init__()
        self.width = 4
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.colour = (139, 0, 0)
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()

        #define its positioninig and velocity
        self.velx = 7
        self.vely = 0

    def update(self):
        self.rect.x +=  self.velx
        self.rect.y +=  self.vely