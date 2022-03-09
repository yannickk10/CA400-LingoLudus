import pygame
from settings import *
from enemy import Enemy
from spanish_vocab import spanish_vehicles


class EnemySpawner:
        def __init__(self):
            self.enemy_group = pygame.sprite.Group()
            self.spawn_timer  = 120

        def update(self):
            self.enemy_group.update()
            if self.spawn_timer == 0:
                self.spawn_enemy()
                self.spawn_timer = 120
            else:
                self.spawn_timer -= 1
