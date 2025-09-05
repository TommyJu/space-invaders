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

    def update(self, x_direction):
        self.rect.x += x_direction

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

def check_collision(aliens, x_direction):
    for alien in aliens:
        # Horizontal collision
        if alien.rect.left <= 0 or alien.rect.right >= screen_size.SCREEN_WIDTH:
            shift_aliens_down(aliens)
            return x_direction * -1
    return x_direction

def shift_aliens_down(aliens):
    for alien in aliens:
        alien.rect.y += alien_constants.COLLISION_Y_SHIFT

def create_laser(aliens):
    if aliens:
        random_alien = choice(aliens.sprites())
        return Laser(random_alien.rect.center, alien_constants.LASER_SPEED, alien_constants.LASER_COLOR)
