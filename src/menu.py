import pygame, select_language
from settings import *
import sys

pygame.init()
# screen resolution
res = (1280, 720)
pygame.display.set_caption("Lingo Ludus")

BG = pygame.image.load("images/purp_background.png")
# opens up a window
SCREEN = pygame.display.set_mode(res)
