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

#High Score Text
high_score_text = header_font.render("High Score", False, (255,255,255))
high_score_box = high_score_text.get_rect()

#Highest Streak Text
highest_streak_text = header_font.render("Highest Streak", False, (255,255,255))
highest_streak_box = highest_streak_text.get_rect()  

#Best Word Text
best_words_text = header_font.render("Best Words", False, (255,255,255))
best_words_box = best_words_text.get_rect()  

#Worst words Text
worst_words_text = header_font.render("Worst Words", False, (255,255,255))
worst_words_box = worst_words_text.get_rect()  

background = pygame.image.load("images/background.png")

gameLoop = True

while gameLoop:
    
    screen.fill("#F8F0E3")
        
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
            pygame.quit()

    screen.blit(background, (0,0))
    
    screen.blit(title_text, ((SCREEN_WIDTH / 2 - title_box.width / 2), 20))

    screen.blit(high_score_text, (((SCREEN_WIDTH // 5 * 1) - high_score_box.width / 2), SCREEN_HEIGHT / 2))
    screen.blit(best_words_text, (((SCREEN_WIDTH // 5 * 1) - best_words_box.width / 2), (SCREEN_HEIGHT / 8) * 6))

    screen.blit(highest_streak_text, (((SCREEN_WIDTH // 5 * 4) - highest_streak_box.width / 2), SCREEN_HEIGHT / 2))
    screen.blit(worst_words_text, (((SCREEN_WIDTH // 5 * 4) - worst_words_box.width / 2), (SCREEN_HEIGHT / 8) * 6))
    
    
    pygame.display.update()
