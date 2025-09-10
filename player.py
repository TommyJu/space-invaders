import pygame
from constants import screen_size
from laser import Laser
from audio_manager import AudioManager

# Represents the player sprite by inheriting from pygame's sprite class.
class Player(pygame.sprite.Sprite):
    MOVEMENT_SPEED = 5
    LASER_COOLDOWN = 600
    STARTING_LIVES = 3

    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load('assets/graphics/space_ship.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)

        # Player lasers
        self.laser_ready = True
        self.laser_fire_time = 0
        self.lasers = pygame.sprite.Group()
        # Player lives
        self.lives = self.STARTING_LIVES


    def get_input(self):
        keys = pygame.key.get_pressed()

        # Horizontal player movement
        if keys[pygame.K_RIGHT] and self.rect.x < (screen_size.SCREEN_WIDTH - self.rect.width):
            self.rect.x += self.MOVEMENT_SPEED
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.MOVEMENT_SPEED

        # Laser input handling and timer start
        if keys[pygame.K_SPACE] and self.laser_ready:
            self.shoot_laser()
            # Disable the laser and log the fire time to enforce laser cooldown
            self.laser_ready = False
            self.laser_fire_time = pygame.time.get_ticks()

    # Laser timer logic
    def laser_recharge(self):
        current_time = pygame.time.get_ticks()
        if current_time > self.laser_fire_time + self.LASER_COOLDOWN:
            self.laser_ready = True

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center))
        AudioManager.play_laser_sound()

    def damage(self, amount=1):
        self.lives = max(0, self.lives - amount)

    def is_dead(self):
        return self.lives <= 0

    def update(self):
        self.get_input()
        self.laser_recharge()
        self.lasers.update()
