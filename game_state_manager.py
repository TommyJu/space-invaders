import pygame
from game_states import WAVE_CLEARED, PLAYING, GAME_OVER
from events import WAVE_CLEARED_EVENT, GAME_OVER_EVENT
from constants import screen_size

# Manages the current state of the game and provides ways to check for game state changes
class GameStateManager:
    
    def __init__(self):
        self.game_state = PLAYING
        self.waves_cleared = 0

    # Mutators for game state
    def switch_game_state_wave_cleared(self):
        self.game_state = WAVE_CLEARED
    
    def switch_game_state_playing(self):
        self.game_state = PLAYING

    def switch_game_state_game_over(self):
        self.game_state = GAME_OVER

    def increment_waves_cleared(self):
        self.waves_cleared += 1

    # Game state checks
    
    def check_game_over(player, aliens):
        if player.is_dead():
            pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))

        
        for alien in aliens:
            if alien.rect.bottom >= screen_size.SCREEN_HEIGHT:
                pygame.event.post(pygame.event.Event(GAME_OVER_EVENT))
    
    def check_wave_cleared(aliens):
        if not aliens:
            pygame.event.post(pygame.event.Event(WAVE_CLEARED_EVENT))