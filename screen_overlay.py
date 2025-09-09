import pygame
from constants import screen_size

class ScreenOverlay:
    GAME_OVER_FONT_SIZE = 20
    FONT_PATH = './assets/font/Pixeled.ttf'
    def wave_clear():
        pass

    def game_over(screen):
        game_over_font = pygame.font.Font(ScreenOverlay.FONT_PATH, ScreenOverlay.GAME_OVER_FONT_SIZE)
        message = game_over_font.render("GAME OVER", False, "white")
        game_over_rect = message.get_rect(center = (screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT / 2))
        screen.blit(message, game_over_rect)

