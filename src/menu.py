import pygame, select_language, achievments_display, game_sel_menu
from pygame import mixer
from settings import *
from button import Button2
import sys

pygame.init()
# screen resolution
res = (SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("Lingo Ludus")

BG = pygame.image.load("assets/images/background.png")
# opens up a window
SCREEN = pygame.display.set_mode(res)
screen_rect = SCREEN.get_rect()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

logo = pygame.image.load("assets/images/lingoludus_logo.png").convert_alpha()
lingo_logo = pygame.transform.scale(logo, (720,250))
menu_rect = lingo_logo.get_rect(center=(SCREEN_WIDTH / 2, 100))

play_button = Button2(image=pygame.image.load("assets/images/play_rect.png"), pos=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 4) * 1 + 50), 
                    text_input="PLAY", font=get_font(60), base_color="White", hovering_color="Orange")
achievments_button = Button2(image=pygame.image.load("assets/images/achievments_rect.png"), pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2+ 50), 
                    text_input="ACHIEVMENTS", font=get_font(60), base_color="White", hovering_color="Orange")

quit_button = Button2(image=pygame.image.load("assets/images/quit_rect.png"), pos=(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 4) * 3 + 50), 
                    text_input="QUIT", font=get_font(60), base_color="White", hovering_color="Red")

#Load sound
forward_sound = mixer.Sound("assets/music/forward_click.wav")
back_sound = mixer.Sound("assets/music/back_click.wav")


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        SCREEN.blit(lingo_logo, menu_rect)

        for button in [play_button, achievments_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    forward_sound.play()
                    select_language.language_select(True)
                if achievments_button.checkForInput(mouse_pos):
                    forward_sound.play()
                    achievments_display.achievments_display_french()
                if quit_button.checkForInput(mouse_pos):
                    back_sound.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
