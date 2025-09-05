import pygame
import screen_size
from laser import Laser

# Represents the player sprite by inheriting from pygame's sprite class.
class Player(pygame.sprite.Sprite):
    MOVEMENT_SPEED = 5
    LASER_COOLDOWN = 600

    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load('assets/graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        
        self.laser_ready = True
        self.laser_fire_time = 0
        self.lasers = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()

        # Horizontal player movement
        if keys[pygame.K_RIGHT] and self.rect.x < (screen_size.SCREEN_WIDTH - self.rect.width):
            self.rect.x += self.MOVEMENT_SPEED
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.MOVEMENT_SPEED

        # Laser beam =====
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.shoot_laser()
            # Disable the laser and log the fire time to enforce laser cooldown
            self.laser_ready = False
            self.laser_fire_time = pygame.time.get_ticks()

    # Readies the laser after a set cooldown time
    def laser_recharge(self):
        current_time = pygame.time.get_ticks()
        if current_time > self.laser_fire_time + self.LASER_COOLDOWN:
            self.laser_ready = True

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center))

    def update(self):
        self.get_input()
        self.laser_recharge()
        self.lasers.update()
