# Import the pygame module
import pygame, sys, random
from pygame import mixer
from pause_menu import pause_menu
from ship import Player
from enemy_spawner import EnemySpawner
from alert_box import AlertBox
from button import *
from settings import *
from french_stats import *
from spanish_stats import *
from vocab import *

def space_invaders(level):

    class PauseButton(Button):

        def draw(self):
            self.top_rectangle.y = self.original_y_position - self.elevation_copy
            self.text_rect.center = self.top_rectangle.center
            
            self.bottom_rectangle.midtop = self.top_rectangle.midtop
            self.bottom_rectangle.height = self.top_rectangle.height + self.elevation_copy

            pygame.draw.rect(screen,self.bottom_rectangle_color, self.bottom_rectangle, border_radius=12)

            pygame.draw.rect(screen,self.top_rectangle_color, self.top_rectangle, border_bottom_right_radius=12, border_top_left_radius=12)
            screen.blit(self.text_surf, self.text_rect)
            if self.if_pressed() == True:
                return False

        def if_pressed(self):
            mouse_position = pygame.mouse.get_pos()
            if self.top_rectangle.collidepoint(mouse_position):
                self.top_rectangle_color = '#D74B4B'
                if pygame.mouse.get_pressed()[0]:
                    self.elevation_copy = 0
                    self.pressed = True
                else:
                    if self.pressed == True:
                        self.pressed = False
                        self.elevation_copy = self.orig_elevation
                        return True
            else:
                self.top_rectangle_color = '#475F77'
                self.elevation_copy = self.orig_elevation

    def game_over_alert(group, max_streak):
        game_over_message = AlertBox("Game Over")
        group.add(game_over_message)
        max_streak += 1

        if not temp_word_stats_dict:
            pass
        else:
            if language == "french":
                filename = "french_stats.py"
            else:
                filename = "spanish_stats.py"
                # update stats file with new player records
            with open(filename, 'w') as f:
                last_item = (list(temp_word_stats_dict.keys())[-1])
                

                # Update the word stats dictionary 
                if language == "french":
                    f.write("word_stats_french = {")
                else:
                    f.write("word_stats_spanish = {")

                for key in (list(temp_word_stats_dict.keys())[:-1]):
                    f.write("'" + key + "'" + " : " + "'" + str(temp_word_stats_dict[key]) + "'" + ",\n")
                
                f.write("'" + last_item + "'"  + " : " + "'" + str(temp_word_stats_dict[last_item]) + "'")
                

                # Update the highscore
                f.write("\n}")
                if language == "french":
                    if player.hud.score_object.score > int(french_highscore):
                        f.write("\n\n" + "french_highscore = "+ "'" + str(player.hud.score_object.score) + "'")
                    else:
                        f.write(("\n\n" + "french_highscore = "+ "'" + str(french_highscore) + "'"))
                else:
                    if player.hud.player_score.score > int(spanish_highscore):
                        f.write("\n\n" + "spanish_highscore = "+ "'" + str(player.hud.score_object.score))
                    else:
                        f.write(("\n\n" + "spanish_highscore = "+ "'" + str(spanish_highscore) + "'"))
                

                # Update the highest streak
                if language == "french":
                    if int(max_streak) > int(french_highest_streak):
                        f.write(("\n\n" + "french_highest_streak = "+ "'" + str(max_streak) + "'"))
                    else:
                        f.write(("\n\n" + "french_highest_streak = "+ "'" + str(french_highest_streak) + "'"))
                else:
                    if int(max_streak) > int(spanish_highest_streak):
                        f.write(("\n\n" + "spanish_highest_streak = "+ "'" + str(max_streak) + "'"))
                    else:
                        f.write(("\n\n" + "spanish_highest_streak = "+ "'" + str(spanish_highest_streak) + "'"))

    class ParticlesShip:
        def __init__(self):
            self.particles = []

        # function to move and draw the particles onto the screen
        def emit(self):
            if self.particles:
                self.delete_particles()
                for particle in self.particles:
                    particle[0][1] += particle[2][0]
                    particle[0][0] += particle[2][1]
                    particle[1] -= 0.2
                    pygame.draw.circle(screen,pygame.Color('White'),particle[0], int(particle[1]))

        # function to add the particles
        def add_particles(self):
            pos_x = player.rect.x
            pos_y = player.rect.y + 30
            radius = 8
            direction_x = random.randint(-3,3)
            direction_y = random.randint(-3,3)
            particle_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]
            self.particles.append(particle_circle)

        # deletes particles after a certain time
        def delete_particles(self):
            particle_copy = [particle for particle in self.particles if particle[1] > 0]
            self.particles = particle_copy
                    
    # Initialize pygame
    pygame.init()

    max_streak = 0

    #Background music
    mixer.music.load("music/background.wav")
    mixer.music.play(-1)

    pressed_keys = pygame.key.get_pressed()

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate player. Right now, this is just a rectangle.
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    enemy_spawner = EnemySpawner(level)
    alert_box_group = pygame.sprite.Group()

    #Create Pause Game Button
    pause_button = PauseButton('ll',pygame.font.Font(None, 30), 60, 40, (15, 15), 6, screen)

    #Create Back to main menu Button
    back_to_game_menu_button = Button('Back to Level Select',pygame.font.Font("assets/font.ttf", 30), 600, 40, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 + 40), 6, screen)

    #Create duplicate word stats dict
    if language == "french":
        temp_word_stats_dict = word_stats_french
    else:
        temp_word_stats_dict = word_stats_spanish


    #Create duplicate best w


    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()
    background_image = pygame.image.load("Sprites/bg_stars1.png").convert()
    x = 0

    partical1 = ParticlesShip()
    PARTICAL_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(PARTICAL_EVENT,40)

    # Variable to keep the main loop gameLoop
    gameLoop = True
    # Main loop
    while gameLoop:
        option = ""

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == pygame.KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == pygame.K_ESCAPE:
                    screen.fill((0,0,0))
                    pygame.mixer.music.pause()
                    pause_sound = mixer.Sound("music/pause.wav")
                    pause_sound.play()
                    option = pause_menu()

            if event.type == PARTICAL_EVENT:
                if player.health != 0:
                    partical1.add_particles()

            # Check for QUIT event. If QUIT, then set gameLoop to false.
            elif event.type == pygame.QUIT:
                screen.fill((0,0,0))
                pygame.mixer.music.stop()
                gameLoop = False
                break

        #Pause Game
        if pause_button.draw() == False:
            pygame.mixer.music.pause()
            pause_sound = mixer.Sound("music/pause.wav")
            pause_sound.play()
            option = pause_menu()
        
        if option == "End Game":
            gameLoop = False
        else:
            pass

        #collision detection

        #bullet and enemy
        bullet_enemy_collision = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
        for bullet, enemy in bullet_enemy_collision.items():
            player.hud.score_object.update_score(enemy[0].enemy_score)
            if player.hud.streak_object.streak > max_streak:
                max_streak = player.hud.streak_object.streak
                if player.health <= 0:
                    pass
                else:
                    player.hud.streak_object.reset_streak()
            enemy[0].get_hit()
            player.get_hit()
            enemy[0].get_hit()
            incorrect_sound = mixer.Sound("music/incorrect enemy.wav")
            incorrect_sound.play()
            if player.health <= 0:
                #Sound from Zapsplat.com
                player_death_sound = mixer.Sound("music/player_death.wav")
                player_death_sound.play()
                player.kill()
                break

        #bullet and imposter
        bullet_imposter_collision = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_imposter, True, False)
        for bullet, enemy in bullet_imposter_collision.items():
            player.hud.score_object.update_score(enemy[0].imposter_score)
            player.hud.streak_object.update_streak()
            if enemy_spawner.enemy_imposter_name not in temp_word_stats_dict:
                temp_word_stats_dict[enemy_spawner.enemy_imposter_name] = 1
            else:
                for key, value in temp_word_stats_dict.items():
                    if key == enemy_spawner.enemy_imposter_name:
                        temp_word_stats_dict[key] = (int(value) + 1)
            enemy[0].get_hit()
            correct_sound = mixer.Sound("music/correct enemy.wav")
            correct_sound.play()

        #enmy and player
        player_enemy_collision = pygame.sprite.groupcollide(all_sprites, enemy_spawner.enemy_group, False, False)
        for player, enemy in player_enemy_collision.items():
            player.get_hit()
            #Sound from Zapsplat.com
            player_hit_sound = mixer.Sound("music/character hit.wav")
            player_hit_sound.play()

            enemy[0].get_hit()
            if player.health <= 0:
                #Sound from Zapsplat.com
                player_death_sound = mixer.Sound("music/player_death.wav")
                player_death_sound.play()
                player.kill()
                break

        # Player and imposter collision
        player_imposter_collision = pygame.sprite.groupcollide(all_sprites, enemy_spawner.enemy_imposter, False, False)
        for player, enemy in player_imposter_collision.items():
            player.get_hit()
            #Sound from Zapsplat.com
            player_hit_sound = mixer.Sound("music/character hit.wav")
            player_hit_sound.play()

            enemy[0].get_hit()
            if player.health <= 0:
                #Sound from Zapsplat.com
                player_death_sound = mixer.Sound("music/player_death.wav")
                player_death_sound.play()
                player.kill()
                break

        # Draw the player on the screen
        all_sprites.draw(screen)
        player.bullets.draw(screen)
        enemy_spawner.enemy_group.draw(screen)
        enemy_spawner.enemy_imposter.draw(screen)
        player.hud_stats.draw(screen)
        player.hud.player_score.draw(screen)
        player.hud.player_streak.draw(screen)
        player.hud.target_name.draw(screen)
        player.hud.health_bar.draw(screen)
        alert_box_group.draw(screen)
        

        # Update all objects
        all_sprites.update(pressed_keys)
        enemy_spawner.update()
        player.hud.target_name.update(enemy_spawner.enemy_imposter_name)
        player.hud.health_bar.update(player.health)
        alert_box_group.update()
        
        #check for game over
        if player.health == 0:
            pygame.mixer.music.stop()
            game_over_alert(alert_box_group, max_streak)
            if back_to_game_menu_button.draw() == False:
                gameLoop = False


        partical1.emit()
        # Update the display
        pygame.display.update()

        # creating a scrolling effect with background to give the illusion the ship is flying through space
        rel_x = x % background_image.get_rect().width
        screen.blit(background_image, (rel_x - background_image.get_rect().width, 0))
        if rel_x < SCREEN_WIDTH:
            screen.blit(background_image, (rel_x, 0))
        x -= 1
            
        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)
