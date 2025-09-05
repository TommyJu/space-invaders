import pygame
from constants import screen_size

class Laser(pygame.sprite.Sprite):
    DEFAULT_LASER_SPEED = 8
    def __init__(self, pos: tuple[int, int], laser_speed = DEFAULT_LASER_SPEED, laser_color = "cyan"):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill(laser_color)
        self.rect = self.image.get_rect(center = pos)
        self.laser_speed = laser_speed
        self.laser_color = laser_color

    # Removes lasers that have moved beyond the viewport
    def destroy(self):
        if self.rect.y < -self.rect.height or (self.rect.y + self.rect.height) > screen_size.SCREEN_HEIGHT:
            self.kill()

    # Updates laser position and clear off-screen lasers
    def update(self):
        self.rect.y -= self.laser_speed
        self.destroy()