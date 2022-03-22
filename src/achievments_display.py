import pygame
from settings import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Define fonts
title_font = pygame.font.Font("assets/font.ttf", 42)
header_font = pygame.font.Font("assets/font.ttf", 30)


#title text
title_text = title_font.render("Achievements", False, (255,255,255))
title_box = title_text.get_rect()

background = pygame.image.load("images/background.png")

gameLoop = True

while gameLoop:
    
    screen.fill("#F8F0E3")
        
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
            pygame.quit()

    screen.blit(background, (0,0))
    
    screen.blit(title_text, ((SCREEN_WIDTH / 2 - title_box.width / 2), 20))
    
    pygame.display.update()
