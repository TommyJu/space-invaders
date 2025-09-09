import pygame, sys
from game import Game
from player import Player
from constants import screen_size
from constants import alien_constants

if __name__ == '__main__':
    # Initialization and constants
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((screen_size.SCREEN_WIDTH, screen_size.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    game = Game(screen)

    # Creating an event to signal alien laser fire
    ALIEN_LASER = pygame.USEREVENT + 1
    pygame.time.set_timer(ALIEN_LASER, alien_constants.LASER_COOLDOWN)

    # Game loop
    while running:
        for event in pygame.event.get():
            # Ending the game loop in response to QUIT event
            if event.type == pygame.QUIT:
                running = False

            if event.type == ALIEN_LASER:
                game.alien_manager.alien_shoot()

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60
        )
    pygame.quit()
