import pygame
from pygame import mixer
import main_game as game
from settings import *
from button2 import *

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def game_hub():

    # initializing the constructor
    pygame.init()

    # screen resolution
    res = (SCREEN_WIDTH, SCREEN_HEIGHT)

    # opens up a window
    screen = pygame.display.set_mode(res)

    forward_sound = mixer.Sound("music/forward_click.wav")
    back_sound = mixer.Sound("music/back_click.wav")

    #Create Title for screen
    title_heading = get_font(42).render("Choose A Game", False, (255,255,255))
    title_box = title_heading.get_rect()


    #Create Buttons
    vehicle_invaders = Button(image=pygame.image.load("images/play_rect.png"), pos=(256, 540), 
                        text_input="Vehicle Invaders", font=get_font(20), base_color="White", hovering_color="Orange")

    number_invaders = Button(image=pygame.image.load("images/play_rect.png"), pos=(640, 360), 
                            text_input="Number Invaders", font=get_font(20), base_color="White", hovering_color="Orange")

    fruit_invaders = Button(image=pygame.image.load("images/play_rect.png"), pos=(1024, 540), 
                            text_input="Fruit Invaders", font=get_font(20), base_color="White", hovering_color="Orange")

    back_button = Button(image=pygame.image.load("images/go_back_rect.png"), pos=(75, 75), 
                        text_input="<-", font=get_font(30), base_color="White", hovering_color="Red")


    background_image = pygame.image.load("images/background.png").convert()
    gameLoop = True

    # Main loop
    while gameLoop:

        # fills the screen with a color
        screen.blit(background_image, [0,0])

        screen.blit(title_heading, ((SCREEN_WIDTH / 2 - title_box.width / 2), 20))

        mouse_pos = pygame.mouse.get_pos()

        for button in [vehicle_invaders, number_invaders, fruit_invaders, back_button]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                pygame.quit()

            #Check button input
            if ev.type == pygame.MOUSEBUTTONDOWN:
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
