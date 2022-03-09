# Import the pygame module
import pygame
import random
from ship import Player
from enemy_spawner import EnemySpawner
from settings import *


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

def space_invaders():

    # Initialize pygame
    pygame.init()

    pressed_keys = pygame.key.get_pressed()

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate player. Right now, this is just a rectangle.
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    enemy_spawner = EnemySpawner()

    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()
    background_image = pygame.image.load("Sprites/cloud_sky_bg.png").convert()

    # Variable to keep the main loop gameLoop
    gameLoop = True

    # Main loop
    while gameLoop:
        # for loop through the event queue

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == pygame.KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == pygame.K_ESCAPE:
                    screen.fill((0,0,0))
                    gameLoop = False
                    break

            # Check for QUIT event. If QUIT, then set gameLoop to false.
            elif event.type == pygame.QUIT:
                screen.fill((0,0,0))
                gameLoop = False
                break

        # Update all objects
        all_sprites.update(pressed_keys)
        enemy_spawner.update()

        # collision detection
        #bullet and enemy
        bullet_enemy_collision = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
        for bullet, enemy in bullet_enemy_collision.items():
            enemy[0].get_hit()

        #bullet and imposter
        bullet_imposter_collision = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_imposter, True, False)
        for bullet, enemy in bullet_imposter_collision .items():
            enemy[0].get_hit()

        #bullet and enemy
        player_enemy_collision = pygame.sprite.groupcollide(all_sprites, enemy_spawner.enemy_group, False, False)
        for player, enemy in player_enemy_collision.items():
            player.get_hit()
            enemy[0].get_hit()


        # Draw the player on the screen
        all_sprites.draw(screen)
        player.bullets.draw(screen)
        enemy_spawner.enemy_group.draw(screen)
        enemy_spawner.enemy_imposter.draw(screen)



        # Update the display
        pygame.display.update()

        # Fill the screen with black for when game ends
        screen.blit(background_image, [0, 0])

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)
