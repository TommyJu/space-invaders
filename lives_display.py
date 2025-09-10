import pygame
from constants import screen_size
from player import Player

class LivesDisplay:
    LIFE_IMAGE_OFFSET = 2
    LIFE_IMAGE_Y_POS = 16

    def __init__(self, player):
        self.player = player
        self.life_image = pygame.image.load("./assets/graphics/pixel_heart.png").convert_alpha()
        self.life_image = pygame.transform.scale(self.life_image, (40, 40))
        self.life_x_start = screen_size.SCREEN_WIDTH - (self.life_image.get_width() + self.LIFE_IMAGE_OFFSET) * Player.STARTING_LIVES

    def draw(self, screen):
        for life in range(self.player.sprite.lives):
            x = self.life_x_start + life * (self.life_image.get_width() + self.LIFE_IMAGE_OFFSET)
            screen.blit(self.life_image, (x, self.LIFE_IMAGE_Y_POS))