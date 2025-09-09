import pygame
from constants import screen_size

class ScreenOverlay:
    FONT_SIZE = 20
    FONT_PATH = './assets/font/Pixeled.ttf'
    
    def game_over(screen):
        font = pygame.font.Font(ScreenOverlay.FONT_PATH, ScreenOverlay.font_SIZE)
        message = font.render("GAME OVER\nPress ENTER to restart.", False, "white")
        rect = message.get_rect(center = (screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT / 2))
        screen.blit(message, rect)

    def wave_cleared(screen):
        font = pygame.font.Font(ScreenOverlay.FONT_PATH, ScreenOverlay.font_SIZE)
        message = font.render("WAVE CLEARED\nPress ENTER to continue.", False, "white")
        rect = message.get_rect(center = (screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT / 2))
        screen.blit(message, rect)
