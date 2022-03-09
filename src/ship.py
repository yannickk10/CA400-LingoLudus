import pygame
from settings import *
from bullet import Bullet
from heads_up_display import HUD

class Player(pygame.sprite.Sprite):
    def __init__(self):

    #Create the player image
        super(Player, self).__init__()
        self.image = pygame.image.load("Sprites/jet.png").convert()
        self.image.set_colorkey((255,255,255), pygame.RLEACCEL)
        self.rect = self.image.get_rect()

        #Player stats displayed in HUD
        self.hud = HUD()
        self.hud_stats = pygame.sprite.Group()
        self.hud_stats.add(self.hud)
        #creating the bullet group for the ships bullets
        self.bullets = pygame.sprite.Group()
        self.shoot_cooldown = 0


        #player health
        self.health = 5

    def update(self, pressed_keys):
        #update the players movements based on inputs

        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 10)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(10, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT - 100:
            self.rect.bottom = SCREEN_HEIGHT - 100

        if pressed_keys[pygame.K_SPACE]:
            if self.shoot_cooldown == 0:
                self.shoot_bullets()
                self.shoot_cooldown = 13

        for bullet in self.bullets:
            if bullet.rect.x >= SCREEN_WIDTH:
                self.bullets.remove(bullet)

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        #Update player externals
        self.bullets.update()

    def shoot_bullets(self):
        #self.bullet_sound.play()
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width)
        new_bullet.rect.y = self.rect.y + 13
        self.bullets.add(new_bullet)

    def get_hit(self):
        self.health  -= 1
        if self.health < 0:
            self.kill()
