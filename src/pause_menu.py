import pygame
from pygame import mixer
from settings import *
from button import *


def pause_menu():
    
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create resume game button
    resume_game_button = Button('Resume game', pygame.font.Font("assets/font.ttf", 13), 150, 60, (SCREEN_WIDTH // 2 - (150 // 2), (SCREEN_HEIGHT // 6) * 2), 6, screen)

    exit_game_button = Button('Exit game', pygame.font.Font("assets/font.ttf", 13), 150, 60, (SCREEN_WIDTH // 2 - (150 // 2), (SCREEN_HEIGHT // 6) * 4), 6, screen)

    gameLoop = True

    while gameLoop:
            
    # fills the screen with a color
        screen.fill("#F8F0E3")
        
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                pygame.quit()

        # Draw pause_menu buttons
        if resume_game_button.draw() == False:
            pause_sound = mixer.Sound("music/unpause.wav")
            pause_sound.play()
            pygame.mixer.music.unpause()
            gameLoop = False
        
        if  exit_game_button.draw() == False:
            pygame.mixer.music.stop()
            return "End Game"

        # updates the frames of the game
        pygame.display.update()

        clock.tick(60)