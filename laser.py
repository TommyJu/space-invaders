import pygame

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

    # Updates laser position and clear off-screen lasers
    def update(self):
        self.rect.y -= self.LASER_SPEED
        self.destroy()