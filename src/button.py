import pygame
from pygame import mixer

class Button:
    def __init__(self, text, font, width, height, pos, elevation, screen):
        self.top_rectangle = pygame.Rect(pos, (width,height))
        self.top_rectangle_color = '#475F77'

        self.gui_font = font
        self.text_surf = self.gui_font.render(text,True,'white')
        self.text_rect = self.text_surf.get_rect(center = self.top_rectangle.center)

        self.bottom_rectangle = pygame.Rect(pos, (width,elevation))
        self.bottom_rectangle_color = '#354B5E'
        
        self.orig_elevation = elevation
        self.elevation_copy = elevation
        self.original_y_position = pos[1]
        
        self.screen = screen

        self.pressed = False

    def draw(self):
        self.top_rectangle.y = self.original_y_position - self.elevation_copy
        self.text_rect.center = self.top_rectangle.center
        
        self.bottom_rectangle.midtop = self.top_rectangle.midtop
        self.bottom_rectangle.height = self.top_rectangle.height + self.elevation_copy

        pygame.draw.rect(self.screen,self.bottom_rectangle_color, self.bottom_rectangle, border_radius=12)

        pygame.draw.rect(self.screen,self.top_rectangle_color, self.top_rectangle, border_radius=12)
        self.screen.blit(self.text_surf, self.text_rect)
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
                    forward_sound = mixer.Sound("assets/music/forward_click.wav")
                    forward_sound.play()
                    return True
        else:
            self.top_rectangle_color = '#475F77'
            self.elevation_copy = self.orig_elevation

class GoBackButton(Button):

        def draw(self):
            self.top_rectangle.y = self.original_y_position - self.elevation_copy
            self.text_rect.center = self.top_rectangle.center
            
            self.bottom_rectangle.midtop = self.top_rectangle.midtop
            self.bottom_rectangle.height = self.top_rectangle.height + self.elevation_copy

            pygame.draw.rect(self.screen,self.bottom_rectangle_color, self.bottom_rectangle, border_radius=12)

            pygame.draw.rect(self.screen,self.top_rectangle_color, self.top_rectangle, border_bottom_left_radius=12, border_top_left_radius=12)
            self.screen.blit(self.text_surf, self.text_rect)
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

class Button2():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)