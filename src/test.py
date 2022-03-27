# Import the pygame module
import pygame
from pause_menu import pause_menu
from ship import Player
from enemy_spawner import EnemySpawner
from alert_box import AlertBox
from button import *
from settings import *
from stats import *

def space_invaders():

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

    def game_over_alert(group):
        game_over_message = AlertBox("Game Over")
        group.add(game_over_message)

        if not temp_highscore_dict:
            pass
        else:
            # update stats file with new player records
            with open(r"stats.py", 'w') as f:
                last_item = (list(temp_highscore_dict.keys())[-1])
                
                f.write("word_stats = {")
                
                for key in (list(temp_highscore_dict.keys())[:-1]):
                    f.write("'" + key + "'" + " : " + "'" + str(temp_highscore_dict[key]) + "'" + ",\n")
                
                f.write("'" + last_item + "'"  + " : " + "'" + str(temp_highscore_dict[last_item]) + "'")
                
                f.write("\n}")
                if temp_highscore > highscore:
                    f.write("\n\n" + str(player.hud.score_object.score))
                else:
                    f.write(("\n\n" + "highscore = "+ "'" + str(player.hud.score_object.score) + "'"))
                    

    # Initialize pygame
    pygame.init()

    pressed_keys = pygame.key.get_pressed()

    # Create the screen object
    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate player. Right now, this is just a rectangle.
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    enemy_spawner = EnemySpawner()
    alert_box_group = pygame.sprite.Group()

    #Create Pause Game Button
    pause_button = PauseButton('ll',pygame.font.Font(None, 30), 60, 40, (15, 15), 6, screen)


    #Create duplicate best words
    temp_highscore_dict = word_stats

    #Create duplicate best words
    temp_highscore = highscore


    # Setup the clock for a decent framerate
    clock = pygame.time.Clock()
    background_image = pygame.image.load("Sprites/cloud_sky_bg.png").convert()

    # Variable to keep the main loop gameLoop
    gameLoop = True

    # Main loop
    while gameLoop:
        # for loop through the event queue

        # Get all the keys currently pressed
        pressed_keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == pygame.KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == pygame.K_ESCAPE:
                    screen.fill((0,0,0))
                    gameLoop = False
                    break

            # Check for QUIT event. If QUIT, then set gameLoop to false.
            elif event.type == pygame.QUIT:
                screen.fill((0,0,0))
                gameLoop = False
                break

        #Pause Game
        if pause_button.draw() == False:
            pause_menu()

        #collision detection

        #bullet and enemy
        bullet_enemy_collision = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
        for bullet, enemy in bullet_enemy_collision.items():
            player.hud.score_object.update_score(enemy[0].enemy_score)
            enemy[0].get_hit()

        #bullet and imposter
        bullet_imposter_collision = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_imposter, True, False)
        for bullet, enemy in bullet_imposter_collision.items():
            player.hud.score_object.update_score(enemy[0].imposter_score)
            if enemy_spawner.enemy_imposter_name not in temp_highscore_dict:
                temp_highscore_dict[enemy_spawner.enemy_imposter_name] = 1
                print(temp_highscore_dict)
            else:
                for key, value in temp_highscore_dict.items():
                    if key == enemy_spawner.enemy_imposter_name:
                        temp_highscore_dict[key] = (int(value) + 1)
                print(temp_highscore_dict)
            enemy[0].get_hit()

        #bullet and enemy
        player_enemy_collision = pygame.sprite.groupcollide(all_sprites, enemy_spawner.enemy_group, False, False)
        for player, enemy in player_enemy_collision.items():
            player.get_hit()
            enemy[0].get_hit()
            if player.health <= 0:
                player.kill()
                break

        # Draw the player on the screen
        all_sprites.draw(screen)
        player.bullets.draw(screen)
        enemy_spawner.enemy_group.draw(screen)
        enemy_spawner.enemy_imposter.draw(screen)
        player.hud_stats.draw(screen)
        player.hud.player_score.draw(screen)
        player.hud.target_name.draw(screen)
        player.hud.health_bar.draw(screen)
        alert_box_group.draw(screen)

        # Update all objects
        all_sprites.update(pressed_keys)
        enemy_spawner.update()
        player.hud.target_name.update(enemy_spawner.enemy_imposter_name)
        player.hud.health_bar.update(player.health)
        alert_box_group.update()
        if player.health == 0:
            game_over_alert(alert_box_group)


        # Update the display
        pygame.display.update()

        # Fill the screen with black for when game ends
        screen.blit(background_image, [0, 0])
            
        # Ensure program maintains a rate of 30 frames per second
        clock.tick(30)
