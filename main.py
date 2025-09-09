import pygame, sys
from game import Game
from player import Player
from constants import screen_size
from constants import alien_constants
from screen_overlay import ScreenOverlay
from events import GAME_OVER_EVENT, ALIEN_LASER_EVENT, WAVE_CLEARED_EVENT
from game_states import GAME_OVER, WAVE_CLEARED, PLAYING
from audio_manager import AudioManager
from game_state_manager import GameStateManager

if __name__ == '__main__':
    # Initialization and constants
    pygame.init()
    pygame.mixer.init()
    AudioManager.play_background_music()
    screen = pygame.display.set_mode((screen_size.SCREEN_WIDTH, screen_size.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    game = Game(screen)

    # Periodically triggering an event to signal alien laser fire at set intervals
    pygame.time.set_timer(ALIEN_LASER_EVENT, alien_constants.LASER_COOLDOWN)
    
    # Game state
    game_state_manager = GameStateManager()

    # Game loop
    while running:
        # Event handling logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
                running = False

            if event.type == ALIEN_LASER_EVENT:
                game.alien_manager.alien_shoot()

            if event.type == GAME_OVER_EVENT:
                game_state_manager.switch_game_state_game_over()

            if event.type == WAVE_CLEARED_EVENT:
                game_state_manager.switch_game_state_wave_cleared()

            # Handle key press events used to navigate to the next game state
            if event.type == pygame.KEYDOWN:
                # Press enter to restart if game over
                if game_state_manager.game_state == GAME_OVER and event.key == pygame.K_RETURN:
                    
                    # Create a fresh game instance for restart
                    game = Game(screen)
                    
                    game_state_manager.game_state = PLAYING

                # Press enter to continue if wave cleared
                if game_state_manager.game_state == WAVE_CLEARED and event.key == pygame.K_RETURN:
                    # TODO implement logic for keeping score, lives, and increasing difficulty. Then go to next round
                    game_state_manager.increment_waves_cleared()
                    
                    game_state_manager.switch_game_state_playing()
        
        screen.fill((30, 30, 30))
        
        # Show different screens depending on the current game state
        if game_state_manager.game_state == PLAYING:
            game.run()

        elif game_state_manager.game_state == WAVE_CLEARED:
            ScreenOverlay.wave_cleared(screen)
        
        elif game_state_manager.game_state == GAME_OVER:
            ScreenOverlay.game_over(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
