import pygame
from constants import screen_size, alien_constants

# Represents a bonus alien that moves across the screen from either side. 
class Extra(pygame.sprite.Sprite):
    def __init__(self, starting_side):
        super().__init__()
        self.image = pygame.image.load("./assets/graphics/extra.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        # Positioning the alien
        self.x_start = -self.rect.width
        self.speed = alien_constants.EXTRA_ALIEN_SPEED
        if starting_side == "right":
            self.x_start = screen_size.SCREEN_WIDTH
            self.speed = -alien_constants.EXTRA_ALIEN_SPEED

        self.rect.x = self.x_start
        self.rect.y = alien_constants.EXTRA_ALIEN_Y_POSITION

    def update(self):
        self.rect.x += self.speed