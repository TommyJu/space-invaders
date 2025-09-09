import pygame
from constants import screen_size

class ScreenOverlay:
    FONT_SIZE = 20
    FONT_PATH = './assets/font/Pixeled.ttf'
    LINE_SPACING = 100
    
    def game_over(screen):
        font = pygame.font.Font(ScreenOverlay.FONT_PATH, ScreenOverlay.FONT_SIZE)
        
        game_over_message = font.render("GAME OVER", False, "red")
        game_over_rect = game_over_message.get_rect(
            center = (screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT / 2)
            )
        screen.blit(game_over_message, game_over_rect)

        continue_message = font.render("press ENTER to restart.", False, "white")
        continue_rect = continue_message.get_rect(
            center = (screen_size.SCREEN_WIDTH / 2, 
                      (screen_size.SCREEN_HEIGHT / 2) + ScreenOverlay.LINE_SPACING)
            )
        screen.blit(continue_message, continue_rect)

    def wave_cleared(screen):
        font = pygame.font.Font(ScreenOverlay.FONT_PATH, ScreenOverlay.FONT_SIZE)
        message = font.render("WAVE CLEARED\nPress ENTER to continue.", False, "white")
        rect = message.get_rect(center = (screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT / 2))
        screen.blit(message, rect)
