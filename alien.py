import pygame
from random import choice
from constants import alien_constants
from constants import screen_size
from laser import Laser

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = f"assets/graphics/{color}.png"
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, aliens_x_direction):
        self.rect.x += aliens_x_direction
        