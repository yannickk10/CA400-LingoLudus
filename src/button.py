import pygame, sys

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