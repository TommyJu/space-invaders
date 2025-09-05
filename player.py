import pygame
import screen_size

# Represents the player sprite by inheriting from pygame's sprite class.
class Player(pygame.sprite.Sprite):
    MOVEMENT_SPEED = 5

    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load('assets/graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.rect.x < (screen_size.SCREEN_WIDTH - self.rect.width):
            self.rect.x += self.MOVEMENT_SPEED
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.MOVEMENT_SPEED

    def update(self):
        self.get_input()