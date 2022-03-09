import pygame
from settings import *
from enemy import Enemy
from spanish_vocab import spanish_vehicles


class EnemySpawner:
        def __init__(self):
            self.enemy_group = pygame.sprite.Group()
            self.spawn_timer  = 120
