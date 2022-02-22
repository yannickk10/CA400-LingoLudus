import pygame, sys
from platformer_settings import *

class Game:
    def __init__(self):
        self.overworld = Overworld()

    def run(self):
        self

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

gameLoop = True

while gameLoop == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)