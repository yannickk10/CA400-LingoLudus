import pygame
from pygame import mixer
from settings import *
from button import Button2

pygame.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BG = pygame.image.load("assets/images/background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
	return pygame.font.Font("assets/font.ttf", size)

def pause_menu():
    pauseloop = True
    while pauseloop:
    # fills the screen with a color
        SCREEN.blit(BG, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(45).render("PAUSE MENU", True, "Orange")
        menu_rect = menu_text.get_rect(center=(640, 100))

        resume_button = Button2(image=pygame.image.load("assets/images/lang_rect.png"), pos=(640, 250), 
							text_input="RESUME", font=get_font(60), base_color="White", hovering_color="Orange")
        quit_button = Button2(image=pygame.image.load("assets/images/quit_rect.png"), pos=(640, 400), 
							text_input="QUIT", font=get_font(60), base_color="White", hovering_color="Orange")

        SCREEN.blit(menu_text, menu_rect)

        for button in [resume_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.checkForInput(mouse_pos):
                    pause_sound = mixer.Sound("assets/music/unpause.wav")
                    pause_sound.play()
                    pygame.mixer.music.unpause()
                    pauseloop = False
                if quit_button.checkForInput(mouse_pos):
                    pygame.mixer.music.stop()
                    return "End Game"

            
        pygame.display.update()
        clock.tick(60)