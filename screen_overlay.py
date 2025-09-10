import pygame
from constants import screen_size
from high_score import save_high_score, load_high_score

class ScreenOverlay:
    FONT_SIZE = 20
    FONT_PATH = './assets/font/Pixeled.ttf'
    LINE_SPACING = 100
    HIGH_SCORE_MARGIN = 60
    
    def game_over(screen, score):
        font = pygame.font.Font(ScreenOverlay.FONT_PATH, ScreenOverlay.FONT_SIZE)
        
        # Update high score
        high_score = load_high_score()
        if high_score < score:
            save_high_score(score)
        

        game_over_message = font.render("GAME OVER", False, "red")
        game_over_rect = game_over_message.get_rect(
            center = (screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT / 2)
            )
        screen.blit(game_over_message, game_over_rect)

        score_message = font.render(f"score: {score}", False, "white")
        score_rect = score_message.get_rect(
            center = (screen_size.SCREEN_WIDTH / 2, 
                      (screen_size.SCREEN_HEIGHT / 2) - ScreenOverlay.LINE_SPACING)
            )
        screen.blit(score_message, score_rect)

        high_score_message = font.render(f"hi-score: {high_score}", False, "yellow")
        high_score_rect = high_score_message.get_rect(
            center = (screen_size.SCREEN_WIDTH / 2, 
                      (screen_size.SCREEN_HEIGHT / 2) - ScreenOverlay.LINE_SPACING - ScreenOverlay.HIGH_SCORE_MARGIN)
            )
        screen.blit(high_score_message, high_score_rect)

        restart_message = font.render("press ENTER to restart.", False, "white")
        restart_rect = restart_message.get_rect(
            center = (screen_size.SCREEN_WIDTH / 2, 
                      (screen_size.SCREEN_HEIGHT / 2) + ScreenOverlay.LINE_SPACING)
            )
        screen.blit(restart_message, restart_rect)

    def wave_cleared(screen):
        font = pygame.font.Font(ScreenOverlay.FONT_PATH, ScreenOverlay.FONT_SIZE)
        message = font.render("WAVE CLEARED", False, "green")
        rect = message.get_rect(center = (screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT / 2))
        screen.blit(message, rect)

        continue_message = font.render("press ENTER to continue.", False, "white")
        continue_rect = continue_message.get_rect(
            center = (screen_size.SCREEN_WIDTH / 2, 
                      (screen_size.SCREEN_HEIGHT / 2) + ScreenOverlay.LINE_SPACING)
            )
        screen.blit(continue_message, continue_rect)