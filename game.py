from player import Player
import pygame
from constants import screen_size
import obstacle
import alien

# Represents the game logic.
class Game:
    DEFAULT_ALIEN_X_DIRECTION = 1

    def __init__(self, screen: pygame.display):
        # Initializing the screen dependency 
        self.screen = screen
        
        # Initializing the player instance variable
        player_sprite = Player((screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT))
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Initializing obstacles
        self.obstacle_blocks = pygame.sprite.Group()
        self.obstacle_blocks.add(obstacle.create_multiple_obstacles())

        # Initializing aliens
        self.aliens = pygame.sprite.Group()
        self.aliens.add(alien.alien_setup())
        self.aliens_x_direction = self.DEFAULT_ALIEN_X_DIRECTION

    def run(self):
        self.player.update()
        self.aliens.update(self.aliens_x_direction)
        self.aliens_x_direction = alien.check_collision(self.aliens, self.aliens_x_direction)
        self.player.sprite.lasers.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_blocks.draw(self.screen)
        self.aliens.draw(self.screen)

