import pygame, sys
from pygame import mixer
from button import Button2
import game_sel_menu
from settings import *

pygame.init()
# screen resolution
res = (SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("Lingo Ludus")

BG = pygame.image.load("assets/images/background.png")

# opens up a window
SCREEN = pygame.display.set_mode(res)
screen_rect = SCREEN.get_rect()

#Load sounds
forward_sound = mixer.Sound("assets/music/forward_click.wav")
back_sound = mixer.Sound("assets/music/back_click.wav")

def get_font(size):
	return pygame.font.Font("assets/font.ttf", size)

def language_select(play):
    gameLoop = True
    while gameLoop:
        SCREEN.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(45).render("LANGUAGE TO LEARN", True, "Orange")
        menu_rect = menu_text.get_rect(center=(SCREEN_WIDTH / 2, 100))

        french_button = Button2(image=pygame.image.load("assets/images/play_rect.png"), pos=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 3) * 1 + 50), 
                                text_input="FRENCH", font=get_font(60), base_color="White", hovering_color="Orange")
        spanish_button = Button2(image=pygame.image.load("assets/images/lang_rect.png"), pos=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 3) * 2 + 50), 
                                text_input="SPANISH", font=get_font(60), base_color="White", hovering_color="Orange")
        back_button = Button2(image=pygame.image.load("assets/images/go_back_rect.png"), pos=(75, 75), 
                            text_input="X", font=get_font(45), base_color="White", hovering_color="Red")

        SCREEN.blit(menu_text, menu_rect)

        for button in [french_button, spanish_button, back_button]:
            button.changeColor(mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if french_button.checkForInput(mouse_pos):
                    forward_sound.play()
                    with open(r"vocab.py", 'r') as f:
                        data = f.readlines()
                        data[0] = "language = 'french'\n"
                    with open(r"vocab.py", 'w') as f:
                        for number, line in enumerate(data):
                            f.write(line)
                    if play == True:
                        game_sel_menu.game_hub()
                    else:
                        gameLoop = False

                if spanish_button.checkForInput(mouse_pos):
                    forward_sound.play()
                    with open(r"vocab.py", 'r') as f:
                        data = f.readlines()
                        data[0] = "language = 'spanish'\n"
                    with open(r"vocab.py", 'w') as f:
                        for number, line in enumerate(data):
                            f.write(line)
                    if play == True:       
                        game_sel_menu.game_hub()
                    else:
                        gameLoop = False

                if back_button.checkForInput(mouse_pos):
                    back_sound.play()
                    gameLoop = False

        pygame.display.update()
