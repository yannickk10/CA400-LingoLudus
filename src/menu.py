import pygame, select_language, achievments_display
from settings import *
from button2 import Button
import sys

pygame.init()
# screen resolution
res = (1280, 720)
pygame.display.set_caption("Lingo Ludus")

BG = pygame.image.load("images/background.png")
# opens up a window
SCREEN = pygame.display.set_mode(res)
screen_rect = SCREEN.get_rect()

def get_font(size): # Returns Press-Start-2P in the desired size
	return pygame.font.Font("assets/font.ttf", size)

def main_menu():
	while True:
		SCREEN.blit(BG, (0, 0))

		mouse_pos = pygame.mouse.get_pos()

		logo = pygame.image.load("images/lingoludus_logo.png").convert_alpha()
		lingo_logo = pygame.transform.scale(logo, (630,250))
		menu_rect = lingo_logo.get_rect(center=(640, 100))

		play_button = Button(image=pygame.image.load("images/play_rect.png"), pos=(640, 230), 
							text_input="PLAY", font=get_font(60), base_color="White", hovering_color="Orange")
		lang_button = Button(image=pygame.image.load("images/lang_rect.png"), pos=(640, 360), 
							text_input="LANGUAGE", font=get_font(60), base_color="White", hovering_color="Orange")
		
		achievments_button = Button(image=pygame.image.load("images/achievments_rect.png"), pos=(640, 490), 
							text_input="ACHIEVMENTS", font=get_font(60), base_color="White", hovering_color="Orange")
		
		quit_button = Button(image=pygame.image.load("images/quit_rect.png"), pos=(640, 630), 
							text_input="QUIT", font=get_font(60), base_color="White", hovering_color="Red")

		SCREEN.blit(lingo_logo, menu_rect)

		for button in [play_button, lang_button, achievments_button, quit_button]:
			button.changeColor(mouse_pos)
			button.update(SCREEN)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if play_button.checkForInput(mouse_pos):
					select_language.language_select()
				if lang_button.checkForInput(mouse_pos):
					select_language.language_select()
				if achievments_button.checkForInput(mouse_pos):
					achievments_display.achievments_display()
				if quit_button.checkForInput(mouse_pos):
					pygame.quit()
					sys.exit()

		pygame.display.update()

main_menu()
