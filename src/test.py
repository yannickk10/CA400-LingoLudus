# Import the pygame module
import pygame
import random

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
	RLEACCEL,
	K_UP,
	K_DOWN,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
	KEYDOWN,
	QUIT,
)

def space_invaders():

	# Define a player object by extending pygame.sprite.Sprite
	# The surface drawn on the screen is now an attribute of 'player'

	# Move the sprite based on user keypresses
	class Player(pygame.sprite.Sprite):
		def __init__(self):
			super(Player, self).__init__()
			self.surf = pygame.image.load("Sprites/jet.png").convert()
			self.surf.set_colorkey((255,255,255), RLEACCEL)
			self.rect = self.surf.get_rect()

		#Player Health:

			self.player_health = 3

		def update(self, pressed_keys):
			if pressed_keys[K_UP]:
				self.rect.move_ip(0, -10)
			if pressed_keys[K_DOWN]:
				self.rect.move_ip(0, 10)
			if pressed_keys[K_LEFT]:
				self.rect.move_ip(-10, 0)
			if pressed_keys[K_RIGHT]:
				self.rect.move_ip(10, 0)

			# Keep player on the screen
			if self.rect.left < 0:
				self.rect.left = 0
			if self.rect.right > SCREEN_WIDTH:
				self.rect.right = SCREEN_WIDTH
			if self.rect.top <= 0:
				self.rect.top = 0
			if self.rect.bottom >= 620:
				self.rect.bottom = 620
			
			if self.player_health == 0:
				self.kill()

	class Enemy(pygame.sprite.Sprite):
		def __init__(self, sprite, backing_colour):
			super(Enemy, self).__init__()
			self.surf = pygame.image.load(sprite).convert_alpha()
			#self.surf.set_colorkey(backing_colour, RLEACCEL)
			self.rect = self.surf.get_rect(center=(
					random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
					random.randint(0, SCREEN_HEIGHT- 120),))

			self.speed = random.randint(5,6)


		def update(self):
			self.rect.move_ip(-self.speed, 0)
			if self.rect.right <= 0:
				self.kill()


	class EnemySpawner:
		def __init__(self):
			self.enemy_group = pygame.sprite.Group()
			self.spawntimer  = random.randrange(30,120)

		def update(self):
			self.enemy_group.update()
			if self.spawn_timer == 0:
				self.spawn_enemy()
				self.spawntimer = random.randrange(30, 120)

		def spawn_enemy(self):
			new_enemy = Enemy()
			self.enemy_group.add(new_enemy)


	class Health(pygame.sprite.Sprite):
		def __init__(self):
			self.heart_border = pygame.image.load("Sprites/heart_border.png").convert()
			self.heart_bg = pygame.image.load("Sprites/heart_bg.png").convert()
			self.heart = pygame.image.load("Sprites/heart.png").convert()
			self.heart_border.set_colorkey((255, 255, 255), RLEACCEL)
			self.heart_bg.set_colorkey((255, 255, 255), RLEACCEL)
			self.heart.set_colorkey((255, 255, 255), RLEACCEL)
			self.rect = self.heart_border.get_rect(center=(SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50))
		
		def draw_heart(self, pos):
			screen.blit(self.heart_border, pos)
			screen.blit(self.heart_bg, pos)
			screen.blit(self.heart, pos)

		def display_health(self):
			self.draw_heart(self.rect)


	# Initialize pygame
	pygame.init()

	pressed_keys = pygame.key.get_pressed()

	# Create the screen object
	# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Instantiate player. Right now, this is just a rectangle.
	player = Player()
	health = Health()
	enemy_spawner = EnemySpawner() 
	all_sprites = pygame.sprite.Group()
	all_sprites.add(player)

	spanish_vehicles ={
    "projectile":  Enemy("Sprites/projectile.gif", (0,0,0)),
    "cars": Enemy("Sprites/Car.png", (0,0,0)),
    "train": Enemy("Sprites/Train.png", (255,255,255))
	}

	# Setup the clock for a decent framerate
	clock = pygame.time.Clock()
	background_image = pygame.image.load("Sprites/cloud_sky_bg.png").convert()

	# Variable to keep the main loop gameLoop
	gameLoop = True

	# Main loop
	while gameLoop:
		# for loop through the event queue

		AddEnemy = pygame.USEREVENT + 1
		pygame.time.set_timer(AddEnemy, 3500)

		for event in pygame.event.get():
			# Check for KEYDOWN event
			if event.type == KEYDOWN:
				# If the Esc key is pressed, then exit the main loop
				if event.key == K_ESCAPE:
					screen.fill((0,0,0))
					gameLoop = False
					break

			# Check for QUIT event. If QUIT, then set gameLoop to false.
			elif event.type == QUIT:
				screen.fill((0,0,0))
				gameLoop = False
				break


			elif event.type == AddEnemy:
				for vehicles in spanish_vehicles.values():
					enemies.add(vehicles)
					all_sprites.add(vehicles)
					print(spanish_vehicles)
		

		# Get all the keys currently pressed
		pressed_keys = pygame.key.get_pressed()

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
