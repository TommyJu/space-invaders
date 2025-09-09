import pygame
from constants import alien_constants

# Represents and displays the player's score
class Score():
    SCORE_Y_POS = 4
    SCORE_PAD_X = 12
    FONT_SIZE = 16
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font('./assets/font/Pixeled.ttf', self.FONT_SIZE)
    
    def draw(self, screen):
        text_surface = self.font.render(f"Score: {self.score}", False, "white")
        screen.blit(text_surface, (self.SCORE_PAD_X, self.SCORE_Y_POS))
    

    def increment_score_alien_hit(self):
        self.score += alien_constants.ALIEN_POINTS

    def increment_score_extra_alien_hit(self):
        self.score += alien_constants.EXTRA_ALIEN_POINTS