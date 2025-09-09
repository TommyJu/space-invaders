import pygame, sys
from game import Game
from player import Player
from constants import screen_size
from constants import alien_constants
from screen_overlay import ScreenOverlay
from events import GAME_OVER_EVENT, ALIEN_LASER_EVENT, WAVE_CLEARED_EVENT
from game_states import GAME_OVER, WAVE_CLEARED, PLAYING

if __name__ == '__main__':
    # Initialization and constants
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((screen_size.SCREEN_WIDTH, screen_size.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    game = Game(screen)

    # Periodically triggering an event to signal alien laser fire at set intervals
    pygame.time.set_timer(ALIEN_LASER_EVENT, alien_constants.LASER_COOLDOWN)
    
    # Game state
    game_state = PLAYING

    # Game loop
    while running:
        # Event handling logic
        for event in pygame.event.get():
            # Ending the game loop in response to QUIT event
            if event.type == pygame.QUIT:
                running = False

            if event.type == ALIEN_LASER_EVENT:
                game.alien_manager.alien_shoot()

            if event.type == GAME_OVER_EVENT:
                game_state = GAME_OVER

            if event.type == WAVE_CLEARED_EVENT:
                pass

        screen.fill((30, 30, 30))
        
        # Game state conditionals
        if game_state == PLAYING:
            game.run()
        elif game_state == GAME_OVER:
            ScreenOverlay.game_over(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
