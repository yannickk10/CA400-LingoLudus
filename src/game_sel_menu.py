import pygame
from pygame import mixer
import main_game as game
from settings import *
from button2 import *


pygame.init()
# screen resolution
res = (1280, 720)
BG = pygame.image.load("images/background.png")

# opens up a window
SCREEN = pygame.display.set_mode(res)
screen_rect = SCREEN.get_rect()

#Load sounds
forward_sound = mixer.Sound("music/forward_click.wav")
back_sound = mixer.Sound("music/back_click.wav")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def game_hub():
    gameLoop = True
    # Main loop
    while gameLoop:
        SCREEN.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        #Create Title for screen
        title_heading = get_font(45).render("CHOOSE A TOPIC", True, "Orange")
        title_rec = title_heading.get_rect(center=(640, 100))

        #Create Buttons
        vehicle_invaders = Button(image=pygame.image.load("images/play_rect.png"), pos=(256, 540), 
                            text_input="Vehicle Invaders", font=get_font(20), base_color="White", hovering_color="Orange")

        number_invaders = Button(image=pygame.image.load("images/play_rect.png"), pos=(640, 360), 
                                text_input="Number Invaders", font=get_font(20), base_color="White", hovering_color="Orange")

        fruit_invaders = Button(image=pygame.image.load("images/play_rect.png"), pos=(1024, 540), 
                                text_input="Fruit Invaders", font=get_font(20), base_color="White", hovering_color="Orange")

        back_button = Button(image=pygame.image.load("images/go_back_rect.png"), pos=(75, 75), 
                            text_input="<-", font=get_font(30), base_color="White", hovering_color="Red")

        # fills the screen with a color
        SCREEN.blit(title_heading, title_rec)

        for button in [vehicle_invaders, number_invaders, fruit_invaders, back_button]:
            button.changeColor(mouse_pos)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            #Check button input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if vehicle_invaders.checkForInput(mouse_pos):
                    forward_sound.play()
                    game.space_invaders("vehicles")
                if number_invaders.checkForInput(mouse_pos):
                    forward_sound.play()
                    game.space_invaders("numbers")
                if fruit_invaders.checkForInput(mouse_pos):
                    forward_sound.play()
                    game.space_invaders("fruits")

                if back_button.checkForInput(mouse_pos):
                    back_sound.play()
                    gameLoop = False

        # updates the frames of the game
        pygame.display.update()
