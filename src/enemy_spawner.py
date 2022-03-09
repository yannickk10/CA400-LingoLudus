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

            spanish_vehicles_list = list(shuffled_spanish_vehicles.values())
            spanish_vehicles_key_list = list(shuffled_spanish_vehicles.keys())

            #Create new enemies
            i = 0
            while i < 2:
                enemy_sprite = spanish_vehicles_list[random.randint(0,len(spanish_vehicles_list)-2)]
                new_enemy = Enemy(enemy_sprite[0], enemy_sprite[1])

                self.enemy_group.add(new_enemy)
                i += 1
