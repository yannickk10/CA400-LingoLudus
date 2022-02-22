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

	# Define constants for the screen width and height
	SCREEN_WIDTH = 720
	SCREEN_HEIGHT = 720

	# Define a player object by extending pygame.sprite.Sprite
	# The surface drawn on the screen is now an attribute of 'player'

	# Move the sprite based on user keypresses
	class Player(pygame.sprite.Sprite):
		def __init__(self):
			super(Player, self).__init__()
			self.surf = pygame.image.load("Sprites/jet.png").convert()
			self.surf.set_colorkey((255,255,255), RLEACCEL)
			self.rect = self.surf.get_rect()

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
			if self.rect.bottom >= SCREEN_HEIGHT:
				self.rect.bottom = SCREEN_HEIGHT

	class Enemy(pygame.sprite.Sprite):
		def __init__(self):
			super(Enemy, self).__init__()
			self.surf = pygame.image.load("Sprites/projectile.gif")
			self.surf.set_colorkey((0,0,0), RLEACCEL)
			self.rect = self.surf.get_rect(center=(
					random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
					random.randint(0, SCREEN_HEIGHT),))

			self.speed = random.randint(5, 20)


		def update(self):
			self.rect.move_ip(-self.speed, 0)
			if self.rect.right <= 0:
				self.kill()
			

	# Initialize pygame
	pygame.init()

	pressed_keys = pygame.key.get_pressed()

	# Create the screen object
	# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	AddEnemy = pygame.USEREVENT + 1
	pygame.time.set_timer(AddEnemy, 250)

	# Instantiate player. Right now, this is just a rectangle.
	player = Player()
	enemies = pygame.sprite.Group()
	all_sprites = pygame.sprite.Group()
	all_sprites.add(player)

	# Setup the clock for a decent framerate
	clock = pygame.time.Clock()
	background_image = pygame.image.load("Sprites/nightcity.jpg").convert()

	# Variable to keep the main loop gameLoop
	gameLoop = True

	# Main loop
	while gameLoop:
		# for loop through the event queue
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
				new_enemy = Enemy()
				enemies.add(new_enemy)
				all_sprites.add(new_enemy)

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

		if pygame.sprite.spritecollideany(player, enemies):
			player.kill()
			gameLoop = False
		

		# Update the display
		pygame.display.update()
		# Ensure program maintains a rate of 30 frames per second
		clock.tick(30)
