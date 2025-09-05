import pygame
import screen_size

class Laser(pygame.sprite.Sprite):
    LASER_SPEED = 8
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill("white")
        self.rect = self.image.get_rect(center = pos)

    # Removes lasers that have moved beyond the viewport
    def destroy(self):
        if self.rect.y < -self.rect.height:
            self.kill()

    def update(self):
        print(self.rect.y)
        # Move the lazer upward upon firing
        self.rect.y -= self.LASER_SPEED
        self.destroy()