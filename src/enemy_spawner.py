import pygame
import importlib
from pygame import mixer
from settings import *
from enemy import Enemy
import vocab
import random

class EnemySpawner:
        def __init__(self, level):
            self.level = level
            self.enemy_group = pygame.sprite.Group()
            self.enemy_imposter = pygame.sprite.Group()
            self.spawn_timer  = 50
            self.enemy_imposter_name = None


        def update(self):
            self.enemy_group.update()
            self.enemy_imposter.update()
            if self.spawn_timer == 0:
                self.spawn_enemy()
                self.spawn_timer = 200
            else:
                self.spawn_timer -= 1


        def spawn_enemy(self):

            # Get Language
            importlib.reload(vocab)
            print(vocab.language)
            language = vocab.language

            # Create and shuffle list

            if language == "spanish":
                if self.level == "numbers":
                    spanish_vehicles_lis = list(vocab.spanish_numbers.items())
                elif self.level == "clothing":
                    spanish_vehicles_lis = list(vocab.spanish_clothing.items())
                elif self.level == "fruits":
                    spanish_vehicles_lis = list(vocab.spanish_fruits.items())
                random.shuffle(spanish_vehicles_lis)
                shuffled_spanish_vehicles = dict(spanish_vehicles_lis)

                spanish_vehicles_list = list(shuffled_spanish_vehicles.values())
                spanish_vehicles_key_list = list(shuffled_spanish_vehicles.keys())
            
                #create imposter
                imposter_sprite = spanish_vehicles_list[len(spanish_vehicles_list)-1]
                new_enemy_imposter = Enemy(imposter_sprite[0], imposter_sprite[1])
                self.enemy_imposter.add(new_enemy_imposter)
                imposter_sound = mixer.Sound(imposter_sprite[2])
                imposter_sound.play()

                #Get imposter name
                self.enemy_imposter_name_pos = spanish_vehicles_list.index(imposter_sprite)
                self.enemy_imposter_name = (spanish_vehicles_key_list[self.enemy_imposter_name_pos])

                spanish_vehicles_list = list(shuffled_spanish_vehicles.values())
                spanish_vehicles_key_list = list(shuffled_spanish_vehicles.keys())

                #Create new enemies
                i = 0
                while i < 4:
                    enemy_sprite = spanish_vehicles_list[random.randint(0,len(spanish_vehicles_list)-2)]
                    new_enemy = Enemy(enemy_sprite[0], enemy_sprite[1])

                    self.enemy_group.add(new_enemy)
                    i += 1
                    
            elif language  == "french":
                if self.level == "numbers":
                    french_vehicles_lis = list(vocab.french_numbers.items())
                elif self.level == "clothing":
                    french_vehicles_lis = list(vocab.french_clothing.items())
                elif self.level == "fruits":
                    french_vehicles_lis = list(vocab.french_fruits.items())
                random.shuffle(french_vehicles_lis)
                shuffled_french_vehicles = dict(french_vehicles_lis)

                french_vehicles_list = list(shuffled_french_vehicles.values())
                french_vehicles_key_list = list(shuffled_french_vehicles.keys())
            
                #create imposter
                imposter_sprite = french_vehicles_list[len(french_vehicles_list)-1]
                new_enemy_imposter = Enemy(imposter_sprite[0], imposter_sprite[1])
                self.enemy_imposter.add(new_enemy_imposter)
                imposter_sound = mixer.Sound(imposter_sprite[2])
                imposter_sound.play()

                #Get imposter name
                self.enemy_imposter_name_pos = french_vehicles_list.index(imposter_sprite)
                self.enemy_imposter_name = (french_vehicles_key_list[self.enemy_imposter_name_pos])

                french_vehicles_list = list(shuffled_french_vehicles.values())
                french_vehicles_key_list = list(shuffled_french_vehicles.keys())

                #Create new enemies
                i = 0
                while i < 4:
                    enemy_sprite = french_vehicles_list[random.randint(0,len(french_vehicles_list)-2)]
                    new_enemy = Enemy(enemy_sprite[0], enemy_sprite[1])

                    self.enemy_group.add(new_enemy)
                    i += 1

