import pygame
from settings import *
from button import *

class Pause_game(pygame.sprite.Sprite):
    def __init__(self):
        super(Pause_game, self).__init__()
        self.image = pygame.image.load("Sprites/pause_screen.png").convert()
        self.image.set_colorkey((10, 10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = P_SCREEN_WIDTH // 2 
        self.rect.y = P_SCREEN_HEIGHT - self.rect.height + 20

    def update(self):
        pass

class ResumeGame(GoBackButton):

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
                    return True
        else:
            self.top_rectangle_color = '#475F77'
            self.elevation_copy = self.orig_elevation

