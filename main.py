import pygame, sys
from game import Game
from player import Player

if __name__ == '__main__':
    # Initialization and constants
    pygame.init()
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    game = Game(screen, (SCREEN_WIDTH, SCREEN_HEIGHT))

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
