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


			elif event.type == AddEnemy:
				for vehicles in spanish_vehicles.values():
					enemies.add(vehicles)
					all_sprites.add(vehicles)
					print(spanish_vehicles)

		# Update the player sprite based on user keypresses
		player.update(pressed_keys)

		enemies.update()


		# Fill the screen with black
		screen.blit(background_image, [0, 0])

		# Draw the player on the screen
		for item in all_sprites:
			screen.blit(item.surf, item.rect)
		health.display_health()
		print(enemies)



		# Update the display
		pygame.display.update()
		# Ensure program maintains a rate of 30 frames per second
		clock.tick(30)
