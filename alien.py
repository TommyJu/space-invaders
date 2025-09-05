import pygame
from random import choice
from constants import alien_constants

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        file_path = f"assets/graphics/{color}.png"
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))


# Returns a list of alien sprites
def alien_setup():
    aliens = list()
    for row in range(alien_constants.ROWS):
        for column in range(alien_constants.COLUMNS):
            x = column * alien_constants.X_OFFSET
            y = row * alien_constants.Y_OFFSET
            alien_color = choice(alien_constants.COLORS)
            alien_sprite = Alien(alien_color, x, y)
            aliens.append(alien_sprite)

    return aliens