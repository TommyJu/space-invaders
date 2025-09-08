import pygame

# Represents an old TV style overlay that can be applied to the game screen
class ScreenEffect:
    def __init__(self):
        self.tv = pygame.image.load("./assets/graphics/tv.png").convert_alpha()

    def draw(self, screen):
        screen.blit(self.tv, (0, 0))