import pygame
from stats import highscores_dict
from settings import *

def get_max(lis):
    highest = 0
    new_lis = list(lis)
    for item in new_lis:
        if int(item) > highest:
            highest = int(item)
    return highest

def calc_top_three_words(dict):
    highest = "None 0"
    scnd_highest = "None 0"
    third_highest = "None 0"
    a = []
    
    for name, score in zip(list(highscores_dict.keys()), list(highscores_dict.values())):
        a.append(name + " " + score)
    
    #Get first
    for item in a:
        if int(item[-1]) > int(highest[-1]):
            highest = item
            
    for item in a:
        if int(highest[-1]) >= int(item[-1]) >= int(scnd_highest[-1]) and item[:-1] != highest[:-1]:
            scnd_highest = item
            
    for item in a:
        if (int(scnd_highest[-1]) >= int(item[-1]) >= int(third_highest[-1])) and (item[:-1] != scnd_highest[:-1]) and (item[:-1] !=highest[:-1]):
            third_highest = item

    return highest, scnd_highest, third_highest



top, second, third = calc_top_three_words(highscores_dict)




pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Define fonts
title_font = pygame.font.Font("assets/font.ttf", 42)
header_font = pygame.font.Font("assets/font.ttf", 30)
body_font = pygame.font.Font("assets/font.ttf", 16)


#title text
title_heading = title_font.render("Achievements", False, (255,255,255))
title_box = title_heading.get_rect()

#High Score Text
high_score_sub_heading = header_font.render("High Score:", False, (255,255,255))
high_score_box = high_score_sub_heading.get_rect()

#Highest Streak sub heading
highest_streak_sub_heading = header_font.render("Highest Streak:", False, (255,255,255))
highest_streak_box = highest_streak_sub_heading.get_rect()  

#Best Word sub heading
best_words_sub_heading = header_font.render("Best Words:", False, (255,255,255))
best_words_box = best_words_sub_heading.get_rect()  

#Worst Words sub heading
worst_words_sub_heading = header_font.render("Worst Words:", False, (255,255,255))
worst_words_box = worst_words_sub_heading.get_rect()

#Best Word_ text
best_word = body_font.render(top, False, (255,255,255))
best_word_box = best_word.get_rect()

scnd_best_word = body_font.render(second, False, (255,255,255))
scnd_best_word_box = scnd_best_word.get_rect()

third_best_word = body_font.render(third, False, (255,255,255))
third_best_word_box = third_best_word.get_rect()


background = pygame.image.load("images/background.png")

gameLoop = True

while gameLoop:
    
    screen.fill("#F8F0E3")
        
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
            pygame.quit()

    #Draw Background
    screen.blit(background, (0,0))
    
    #Draw Titles card
    screen.blit(title_heading, ((SCREEN_WIDTH / 2 - title_box.width / 2), 20))

    #Draw sub headings
    screen.blit(high_score_sub_heading, (((SCREEN_WIDTH // 5 * 1) - high_score_box.width / 2), SCREEN_HEIGHT / 2))
   
    screen.blit(best_words_sub_heading, (((SCREEN_WIDTH // 5 * 1) - best_words_box.width / 2), (SCREEN_HEIGHT / 8) * 6))

    screen.blit(highest_streak_sub_heading, (((SCREEN_WIDTH // 5 * 4) - highest_streak_box.width / 2), SCREEN_HEIGHT / 2))
  
    screen.blit(worst_words_sub_heading, (((SCREEN_WIDTH // 5 * 4) - worst_words_box.width / 2), (SCREEN_HEIGHT / 8) * 6))

    #Draw best words text
    screen.blit(best_word, (((SCREEN_WIDTH // 5 * 1) - best_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 55)))
    screen.blit(scnd_best_word, (((SCREEN_WIDTH // 5 * 1) - scnd_best_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 105)))
    screen.blit(third_best_word, (((SCREEN_WIDTH // 5 * 1) - third_best_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 155)))

    
    
    
    pygame.display.update()
