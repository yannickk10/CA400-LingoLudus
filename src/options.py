import pygame, sys, os, glob
from pygame import mixer
from button import Button2
import gettext
from settings import *

pygame.init()


#en = gettext.translation('messages', localedir='locale', languages=['en_US'])
#fr = gettext.translation('messages', localedir='locale', languages=['fr_FR'])

# used to mark translatable string
_ = gettext.gettext

def set_locale(value):
    global locale, translations
    locale = value
    translations[locale].install()
# screen resolution
res = (1280, 720)
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

def options():
    gameLoop = True
    while gameLoop:
        SCREEN.blit(BG, (0, 0))

        # used to mark translatable string
        _ = gettext.gettext


        #en = gettext.translation('messages', localedir='locale', languages=['en_US'])
        #fr = gettext.translation('messages', localedir='locale', languages=['fr_FR'])


        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(45).render(_("APP LANGUAGE"), True, "Orange")
        menu_rect = menu_text.get_rect(center=(640, 100))

        en_button = Button2(image=pygame.image.load("assets/images/play_rect.png"), pos=(640, 250), 
                                text_input=_("ENGLISH"), font=get_font(60), base_color="White", hovering_color="Orange")
        fr_button = Button2(image=pygame.image.load("assets/images/lang_rect.png"), pos=(640, 400), 
                                text_input=_("FRENCH"), font=get_font(60), base_color="White", hovering_color="Orange")
        back_button = Button2(image=pygame.image.load("assets/images/go_back_rect.png"), pos=(75, 75), 
                            text_input="X", font=get_font(45), base_color="White", hovering_color="Red")

        SCREEN.blit(menu_text, menu_rect)

        for button in [en_button, fr_button, back_button]:
            button.changeColor(mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if en_button.checkForInput(mouse_pos):
                    forward_sound.play()
                    set_locale('en_US')

                if fr_button.checkForInput(mouse_pos):
                    forward_sound.play()
                    set_locale('fr_FR')

                if back_button.checkForInput(mouse_pos):
                    back_sound.play()
                    gameLoop = False

        pygame.display.update()

locales = [x.split('\\')[1] for x in glob.glob('locale/*') if os.path.isdir(x)]
active_locale = 'en_US'
translations = {}
for locale in locales:
    translations[locale] = gettext.translation('messages', localedir='locale', languages=[locale])
translations[active_locale].install()

options()
