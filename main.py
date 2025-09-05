import pygame, sys
from game import Game
from player import Player
import screen_size

if __name__ == '__main__':
    # Initialization and constants
    pygame.init()
    screen = pygame.display.set_mode((screen_size.SCREEN_WIDTH, screen_size.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    game = Game(screen)

    # Game loop
    while running:
        for event in pygame.event.get():
            # Ending the game loop in response to QUIT event
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))
        game.run()

        pygame.display.flip()
        clock.tick(60
        )
    pygame.quit()
