import pygame
import game_sel_menu
import button as Button

def language_select():

	class Button:
		def __init__(self, text, width, height, pos,elevation):
			self.top_rectangle = pygame.Rect(pos, (width,height))
			self.top_rectangle_color = '#475F77'

			self.text_surf = gui_font.render(text,True,'#FFFFFF')
			self.text_rect = self.text_surf.get_rect(center = self.top_rectangle.center)

			self.bottom_rectangle = pygame.Rect(pos, (width,elevation))
			self.bottom_rectangle_color = '#354B5E'

			self.orig_elevation = elevation
			self.elevation_copy = elevation
			self.original_y_position = pos[1]

			self.pressed = False

		def draw(self):
			self.top_rectangle.y = self.original_y_position - self.elevation_copy
			self.text_rect.center = self.top_rectangle.center

			self.bottom_rectangle.midtop = self.top_rectangle.midtop
			self.bottom_rectangle.height = self.top_rectangle.height + self.elevation_copy

			pygame.draw.rect(screen,self.bottom_rectangle_color, self.bottom_rectangle, border_radius=12)

			pygame.draw.rect(screen,self.top_rectangle_color, self.top_rectangle, border_radius=12)
			screen.blit(self.text_surf, self.text_rect)
			self.if_pressed()

		def if_pressed(self):
			mouse_position = pygame.mouse.get_pos()
			if self.top_rectangle.collidepoint(mouse_position):
				self.top_rectangle_color = '#D74B4B'
				if pygame.mouse.get_pressed()[0]:
					self.elevation_copy = 0
					self.pressed = True
				else:
					if self.pressed == True:
						print('click')
					self.pressed = False
					self.elevation_copy = self.orig_elevation
			else:
				self.top_rectangle_color = '#475F77'
				self.elevation_copy = self.orig_elevation

	class SpanishButton(Button):

		def draw(self):
			self.top_rectangle.y = self.original_y_position - self.elevation_copy
			self.text_rect.center = self.top_rectangle.center

			self.bottom_rectangle.midtop = self.top_rectangle.midtop
			self.bottom_rectangle.height = self.top_rectangle.height + self.elevation_copy

			pygame.draw.rect(screen,self.bottom_rectangle_color, self.bottom_rectangle, border_radius=12)

			pygame.draw.rect(screen,self.top_rectangle_color, self.top_rectangle, border_radius=12)
			screen.blit(self.text_surf, self.text_rect)
			if self.if_pressed() == True:
				return False

		def if_pressed(self):
			mouse_position = pygame.mouse.get_pos()
			if self.top_rectangle.collidepoint(mouse_position):
				self.top_rectangle_color = '#D74B4B'
				if pygame.mouse.get_pressed()[0]:
					self.elevation_copy = 0
					self.pressed = True
				else:
					if self.pressed == True:
						self.pressed = False
						self.elevation_copy = self.orig_elevation
						return True
			else:
				self.top_rectangle_color = '#475F77'
				self.elevation_copy = self.orig_elevation

	class FrenchButton(Button):

		def draw(self):
			self.top_rectangle.y = self.original_y_position - self.elevation_copy
			self.text_rect.center = self.top_rectangle.center

			self.bottom_rectangle.midtop = self.top_rectangle.midtop
			self.bottom_rectangle.height = self.top_rectangle.height + self.elevation_copy

			pygame.draw.rect(screen,self.bottom_rectangle_color, self.bottom_rectangle, border_radius=12)

			pygame.draw.rect(screen,self.top_rectangle_color, self.top_rectangle, border_radius=12)
			screen.blit(self.text_surf, self.text_rect)
			if self.if_pressed() == True:
				return False

		def if_pressed(self):
			mouse_position = pygame.mouse.get_pos()
			if self.top_rectangle.collidepoint(mouse_position):
				self.top_rectangle_color = '#D74B4B'
				if pygame.mouse.get_pressed()[0]:
					self.elevation_copy = 0
					self.pressed = True
				else:
					if self.pressed == True:
						self.pressed = False
						self.elevation_copy = self.orig_elevation
						return True

			else:
				self.top_rectangle_color = '#475F77'
				self.elevation_copy = self.orig_elevation

	class GoBackButton (Button):

		def draw(self):
			self.top_rectangle.y = self.original_y_position - self.elevation_copy
			self.text_rect.center = self.top_rectangle.center

			self.bottom_rectangle.midtop = self.top_rectangle.midtop
			self.bottom_rectangle.height = self.top_rectangle.height + self.elevation_copy

			pygame.draw.rect(screen,self.bottom_rectangle_color, self.bottom_rectangle, border_radius=12)

			pygame.draw.rect(screen,self.top_rectangle_color, self.top_rectangle, border_bottom_left_radius=12, border_top_left_radius=12)
			screen.blit(self.text_surf, self.text_rect)
			if self.if_pressed() == True:
				return False

		def if_pressed(self):
			mouse_position = pygame.mouse.get_pos()
			if self.top_rectangle.collidepoint(mouse_position):
				self.top_rectangle_color = '#D74B4B'
				if pygame.mouse.get_pressed()[0]:
					self.elevation_copy = 0
					self.pressed = True
				else:
					if self.pressed == True:
						self.pressed = False
						self.elevation_copy = self.orig_elevation
						return True
			else:
				self.top_rectangle_color = '#475F77'
				self.elevation_copy = self.orig_elevation

	# initializing the constructor
	pygame.init()

	# screen resolution
	res = (720,720)

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

	# defining a font
	gui_font = pygame.font.Font(None, 30)

	#create button object

	select_french_button = FrenchButton('French', 200, 40, (width/2-100,300), 6)
	select_spanish_button = SpanishButton('Spanish', 200, 40, (width/2-100,420), 6)
	go_back_button = GoBackButton('Back', 80, 40, (10,670), 6)

	gameLoop = True

	# Main loop
	while gameLoop:

		for ev in pygame.event.get():

			if ev.type == pygame.QUIT:
				pygame.quit()

		# fills the screen with a color
		screen.fill('#F8F0E3')
		screen.blit(background_image, [0,0])

		if select_french_button.draw() == False:
			game_sel_menu.game_hub("Spansih")
		if select_spanish_button.draw() == False:
			game_sel_menu.game_hub("French")

		if go_back_button.draw() == False:
			gameLoop = False



		# updates the frames of the game
		pygame.display.update()
