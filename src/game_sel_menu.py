import pygame
import main_game as gt
import sys
from settings import *
from button import *
import pygame, sys


def game_hub():

	class WordInvadersButton(Button):
		
		def if_pressed(self):
			mouse_position = pygame.mouse.get_pos()
			if self.top_rectangle.collidepoint(mouse_position):
				self.top_rectangle_color = '#D74B4B'
				if pygame.mouse.get_pressed()[0]:
					self.elevation_copy = 0
					self.pressed = True
				else:
					if self.pressed == True:
						gt.space_invaders()
					self.pressed = False
					self.elevation_copy = self.orig_elevation
			else:
				self.top_rectangle_color = '#475F77'
				self.elevation_copy = self.orig_elevation

	# initializing the constructor
	pygame.init()

	# screen resolution
	res = (SCREEN_WIDTH, SCREEN_HEIGHT)

	# opens up a window
	screen = pygame.display.set_mode(res)

	# white color
	white = (255,255,255)

	# light shade of the button
	grey = (170,170,170)

	# dark shade of the button
	black = (100,100,100)

	# stores the width of the
	# screen into a variable
	width = screen.get_width()

	# stores the height of the
	# screen into a variable
	height = screen.get_height()

	pressed_keys = pygame.key.get_pressed()

	background_image = pygame.image.load("images/LiLu_Logo.png").convert()

	word_invaders_button = WordInvadersButton('Play Word Invaders', pygame.font.Font(None, 30), 200, 40, (width/2-100,300), 6, screen)
	go_back_button = GoBackButton('Back', pygame.font.Font(None, 30), 80, 40, (10,670), 6, screen)
	
	gameLoop = True

	# Main loop
	while gameLoop:
		
		for ev in pygame.event.get():
			
			if ev.type == pygame.QUIT:
				pygame.quit()
					
		# fills the screen with a color
		screen.fill('#F8F0E3')
		screen.blit(background_image, [0,0])

		word_invaders_button.draw()
		if go_back_button.draw() == False:
			gameLoop = False
		
		# updates the frames of the game
		pygame.display.update()