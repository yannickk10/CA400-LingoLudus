import pygame
from settings import *
from button import *

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

def pause_menu():
    
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create resume game button
    resume_game_button = ResumeGame('Resume game', pygame.font.Font("assets/font.ttf", 13), 150, 60, (SCREEN_WIDTH // 2 - (150 // 2), SCREEN_HEIGHT // 2 - 80), 6, screen)

    gameLoop = True

    while gameLoop:
            
    # fills the screen with a color
        screen.fill("#F8F0E3")
        
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                pygame.quit()

        # Draw pause_menu buttons
        if resume_game_button.draw() == False:
            gameLoop = False

        # updates the frames of the game
        pygame.display.update()

        clock.tick(60)