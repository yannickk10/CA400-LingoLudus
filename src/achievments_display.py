import pygame
import importlib
from pygame import mixer
from button import Button2
import french_stats
import spanish_stats
from settings import *

def get_font(size):
	return pygame.font.Font("assets/font.ttf", size)

def calc_best_three_words(dict):

    importlib.reload(french_stats)
    importlib.reload(spanish_stats)
    
    highest = "None 0"
    scnd_highest = "None 0"
    third_highest = "None 0"
    a = []
    
    for name, score in zip(list(dict.keys()), list(dict.values())):
        a.append(str(name) + " " + str(score))
    
    #Get first
    for item in a:
        if int(item.split()[-1]) > int(highest.split()[-1]):
            highest = item
            
    for item in a:
        if int(highest.split()[-1]) >= int(item.split()[-1]) >= int(scnd_highest.split()[-1]) and item.split()[:-1] != highest.split()[:-1]:
            scnd_highest = item
            
    for item in a:
        if (int(scnd_highest.split()[-1]) >= int(item.split()[-1]) >= int(third_highest.split()[-1])) and (item.split()[:-1] != scnd_highest.split()[:-1]) and (item.split()[:-1] !=highest.split()[:-1]):
            third_highest = item

    return highest, scnd_highest, third_highest

def calc_worst_three_words(dict):

    importlib.reload(french_stats)
    importlib.reload(spanish_stats)

    lowest = "None 1000000"
    scnd_lowest = "None 1000000"
    third_lowest = "None 1000000"
    a = []
    
    for name, score in zip(list(dict.keys()), list(dict.values())):
        a.append(str(name) + " " + str(score))
    
    #Get first
    for item in a:
        if int(item.split()[-1]) < int(lowest.split()[-1]):
            lowest = item
            
    for item in a:
        if int(lowest.split()[-1]) <= int(item[-1]) <= int(scnd_lowest.split()[-1]) and item[:-1] != lowest.split()[-1]:
            scnd_lowest = item
            
    for item in a:
        if (int(scnd_lowest.split()[-1]) <= int(item.split()[-1]) <= int(third_lowest.split()[-1])) and (item.split()[:-1] != scnd_lowest.split()[:-1]) and (item.split()[:-1] != lowest.split()[:-1]):
            third_lowest = item
    
    if lowest == "None 1000000" and scnd_lowest == "None 1000000" and third_lowest == "None 1000000":
        lowest = "None"
        scnd_lowest = "None"
        third_lowest = "None"

    return lowest, scnd_lowest, third_lowest


def achievments_display_french():

    best_word, second_best_word, third_best_word = calc_best_three_words(french_stats.word_stats_french)

    worst_word, second_worst_word, third_worst_word = calc_worst_three_words(french_stats.word_stats_french)

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    go_right_button = Button2(image=pygame.image.load("assets/images/go_back_rect.png"), pos=(SCREEN_WIDTH - 75, (SCREEN_HEIGHT // 2) - 75), 
                            text_input="->", font=get_font(45), base_color="White", hovering_color="Red")
    go_back_button = Button2(image=pygame.image.load("assets/images/go_back_rect.png"), pos=(75, 75), 
                            text_input="X", font=get_font(45), base_color="White", hovering_color="Red")

    #Define fonts
    header_font = pygame.font.Font("assets/font.ttf", 30)
    body_font = pygame.font.Font("assets/font.ttf", 20)


    #title text
    title_heading = get_font(45).render("FRENCH ACHIEVEMENTS", True, "Orange")
    title_rec = title_heading.get_rect(center=(SCREEN_WIDTH / 2, 100))

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

    #Best Word text
    best_word = body_font.render(best_word, False, (255,255,255))
    best_word_box = best_word.get_rect()

    scnd_best_word = body_font.render(second_best_word, False, (255,255,255))
    scnd_best_word_box = scnd_best_word.get_rect()

    third_best_word = body_font.render(third_best_word, False, (255,255,255))
    third_best_word_box = third_best_word.get_rect()

    #Worst Word text
    worst_word = body_font.render(worst_word, False, (255,255,255))
    worst_word_box = worst_word.get_rect()

    scnd_worst_word = body_font.render(second_worst_word, False, (255,255,255))
    scnd_worst_word_box = scnd_worst_word.get_rect()

    third_worst_word = body_font.render(third_worst_word, False, (255,255,255))
    third_worst_word_box = third_worst_word.get_rect()

    #HighScore Text
    highest_score = body_font.render(french_stats.french_highscore, False, (255,255,255))
    highest_score_text_box = highest_score.get_rect()

    #HighStreak Text
    highest_streak_text = body_font.render(french_stats.french_highest_streak, False, (255,255,255))
    streak_box = highest_streak_text.get_rect()

    background = pygame.image.load("assets/images/background.png")

    #Load sounds
    forward_sound = mixer.Sound("assets/music/forward_click.wav")
    back_sound = mixer.Sound("assets/music/back_click.wav")

    gameLoop = True

    while gameLoop:
        
        screen.fill("#F8F0E3")
            
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                pygame.quit()

        #Draw Background
        screen.blit(background, (0,0))
        
        #Draw Titles card
        screen.blit(title_heading, title_rec)

        #Draw sub headings
        screen.blit(high_score_sub_heading, (((SCREEN_WIDTH // 5 * 1) - high_score_box.width / 2), SCREEN_HEIGHT / 2))
        screen.blit(best_words_sub_heading, (((SCREEN_WIDTH // 5 * 1) - best_words_box.width / 2), (SCREEN_HEIGHT / 8) * 6))

        screen.blit(highest_streak_sub_heading, (((SCREEN_WIDTH // 5 * 4) - highest_streak_box.width / 2), SCREEN_HEIGHT / 2))
    
        screen.blit(worst_words_sub_heading, (((SCREEN_WIDTH // 5 * 4) - worst_words_box.width / 2), (SCREEN_HEIGHT / 8) * 6))

        #Draw highscore text

        screen.blit(highest_score, (((SCREEN_WIDTH // 5 * 1) - highest_score_text_box.width / 2), (SCREEN_HEIGHT / 2) + 55))

        #Draw best words text
        screen.blit(best_word, (((SCREEN_WIDTH // 5 * 1) - best_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 55)))
        screen.blit(scnd_best_word, (((SCREEN_WIDTH // 5 * 1) - scnd_best_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 105)))
        screen.blit(third_best_word, (((SCREEN_WIDTH // 5 * 1) - third_best_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 155)))

        #Draw worst words text
        screen.blit(worst_word, (((SCREEN_WIDTH // 5 * 4) - worst_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 55)))
        screen.blit(scnd_worst_word, (((SCREEN_WIDTH // 5 * 4) - scnd_worst_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 105)))
        screen.blit(third_worst_word, (((SCREEN_WIDTH // 5 * 4) - third_worst_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 155))) 

        #Draw highest streak
        screen.blit(highest_streak_text, (((SCREEN_WIDTH // 5 * 4) - streak_box.width / 2), (SCREEN_HEIGHT / 2) + 55))

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(title_heading, title_rec)

        for button in [go_right_button, go_back_button]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #Check button input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_right_button.checkForInput(mouse_pos):
                    forward_sound.play()
                    achievments_display_spanish()
                if go_back_button.checkForInput(mouse_pos):
                    back_sound.play()
                    gameLoop = False
    
        # updates the frames of the game
        pygame.display.update()

def achievments_display_spanish():

    best_word, second_best_word, third_best_word = calc_best_three_words(spanish_stats.word_stats_spanish)

    worst_word, second_worst_word, third_worst_word = calc_worst_three_words(spanish_stats.word_stats_spanish)
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    go_back_button = Button2(image=pygame.image.load("assets/images/go_back_rect.png"), pos=(75, 75), 
                            text_input="X", font=get_font(45), base_color="White", hovering_color="Red")

    go_left_button = Button2(image=pygame.image.load("assets/images/go_back_rect.png"), pos=(75, (SCREEN_HEIGHT // 2) - 75), 
                            text_input="<-", font=get_font(45), base_color="White", hovering_color="Red")

    #Define fonts
    header_font = pygame.font.Font("assets/font.ttf", 30)
    body_font = pygame.font.Font("assets/font.ttf", 20)


    #title text
    title_heading = get_font(45).render("SPANISH ACHIEVEMENTS", True, "Orange")
    title_rec = title_heading.get_rect(center=(640, 100))

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

    #Best Word text
    best_word = body_font.render(best_word, False, (255,255,255))
    best_word_box = best_word.get_rect()

    scnd_best_word = body_font.render(second_best_word, False, (255,255,255))
    scnd_best_word_box = scnd_best_word.get_rect()

    third_best_word = body_font.render(third_best_word, False, (255,255,255))
    third_best_word_box = third_best_word.get_rect()

    #Worst Word text
    worst_word = body_font.render(worst_word, False, (255,255,255))
    worst_word_box = worst_word.get_rect()

    scnd_worst_word = body_font.render(second_worst_word, False, (255,255,255))
    scnd_worst_word_box = scnd_worst_word.get_rect()

    third_worst_word = body_font.render(third_worst_word, False, (255,255,255))
    third_worst_word_box = third_worst_word.get_rect()

    #HighScore Text
    highest_score = body_font.render(spanish_stats.spanish_highscore, False, (255,255,255))
    highest_score_box = highest_score.get_rect()

    #HighStreak Text
    highest_streak_text = body_font.render(spanish_stats.spanish_highest_streak, False, (255,255,255))
    streak_box = highest_streak_text.get_rect()

    background = pygame.image.load("assets/images/background.png")

    #Load sounds 
    forward_sound = mixer.Sound("assets/music/forward_click.wav")
    back_sound = mixer.Sound("assets/music/back_click.wav")

    gameLoop = True

    while gameLoop:
        
        screen.fill("#F8F0E3")
            
        for ev in pygame.event.get():
            
            if ev.type == pygame.QUIT:
                pygame.quit()

        #Draw Background
        screen.blit(background, (0,0))
        
        #Draw Titles card
        screen.blit(title_heading, title_rec)

        #Draw sub headings
        screen.blit(high_score_sub_heading, (((SCREEN_WIDTH // 5 * 1) - high_score_box.width / 2), SCREEN_HEIGHT / 2))
        screen.blit(best_words_sub_heading, (((SCREEN_WIDTH // 5 * 1) - best_words_box.width / 2), (SCREEN_HEIGHT / 8) * 6))

        screen.blit(highest_streak_sub_heading, (((SCREEN_WIDTH // 5 * 4) - highest_streak_box.width / 2), SCREEN_HEIGHT / 2))
    
        screen.blit(worst_words_sub_heading, (((SCREEN_WIDTH // 5 * 4) - worst_words_box.width / 2), (SCREEN_HEIGHT / 8) * 6))

        #Draw highscore text

        screen.blit(highest_score, (((SCREEN_WIDTH // 5 * 1) - highest_score_box.width / 2), (SCREEN_HEIGHT / 2) + 55))

        #Draw best words text
        screen.blit(best_word, (((SCREEN_WIDTH // 5 * 1) - best_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 55)))
        screen.blit(scnd_best_word, (((SCREEN_WIDTH // 5 * 1) - scnd_best_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 105)))
        screen.blit(third_best_word, (((SCREEN_WIDTH // 5 * 1) - third_best_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 155)))

        #Draw worst words text
        screen.blit(worst_word, (((SCREEN_WIDTH // 5 * 4) - worst_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 55)))
        screen.blit(scnd_worst_word, (((SCREEN_WIDTH // 5 * 4) - scnd_worst_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 105)))
        screen.blit(third_worst_word, (((SCREEN_WIDTH // 5 * 4) - third_worst_word_box.width / 2), ((SCREEN_HEIGHT / 8) * 6 + 155)))

        #Draw highest streak
        screen.blit(highest_streak_text, (((SCREEN_WIDTH // 5 * 4) - streak_box.width / 2), (SCREEN_HEIGHT / 2) + 55))

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(title_heading, title_rec)

        for button in [go_left_button, go_back_button]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #Check button input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_left_button.checkForInput(mouse_pos):
                    forward_sound.play()
                    gameLoop = False
                if go_back_button.checkForInput(mouse_pos):
                    back_sound.play()
                    gameLoop = False
        # updates the frames of the game
        pygame.display.update()
