import pygame, select_language
from settings import *
from button2 import Button
import sys

pygame.init()
# screen resolution
res = (1280, 720)
pygame.display.set_caption("Lingo Ludus")

BG = pygame.image.load("images/purp_background.png")
# opens up a window
SCREEN = pygame.display.set_mode(res)

def get_font(size): # Returns Press-Start-2P in the desired size
	return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        play_button = Button(image=pygame.image.load("images/play_rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Orange")
        lang_button = Button(image=pygame.image.load("images/lang_rect.png"), pos=(640, 400), 
                            text_input="LANGUAGE", font=get_font(75), base_color="#d7fcd4", hovering_color="Orange")
        quit_button = Button(image=pygame.image.load("images/quit_rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Orange")
