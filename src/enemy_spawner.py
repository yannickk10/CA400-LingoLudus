import pygame
from settings import *
from enemy import Enemy
from spanish_vocab import spanish_vehicles
import random


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


        def spawn_enemy(self):
            #create and shuffle list
            spanish_vehicles_lis = list(spanish_vehicles.items())
            random.shuffle(spanish_vehicles_lis)
            shuffled_spanish_vehicles = dict(spanish_vehicles_lis)
