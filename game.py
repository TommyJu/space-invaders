from player import Player
import pygame
from constants import screen_size
import obstacle
from random import randint, choice
import collision
import alien_manager
import lives_display
import score
import screen_effect


# Represents the game logic.
class Game:
    def __init__(self, screen: pygame.display):
        # Initializing the screen dependency 
        self.screen = screen
        
        # Initializing the player instance variable
        player_sprite = Player((screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT))
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Initializing obstacles
        self.obstacle_blocks = pygame.sprite.Group()
        self.obstacle_blocks.add(obstacle.create_multiple_obstacles())

        # Initializing alien manager
        self.alien_manager = alien_manager.AlienManager()

        # Initializing player lives UI
        self.lives_display = lives_display.LivesDisplay(self.player)

        # Initializing game score
        self.score = score.Score()

        self.screen_effect = screen_effect.ScreenEffect()

    def run(self):
        # Updating game state
        self.player.update()
        self.alien_manager.update()
        # Collision checks
        aliens_direction = collision.alien_screen_collision(self.alien_manager.aliens, self.alien_manager.aliens_x_direction)
        self.alien_manager.set_aliens_x_direction(aliens_direction)
        collision.handle_side_effect_collisions(self.player, self.obstacle_blocks, self.alien_manager, self.score)
        # Drawing sprites to the screen
        self.screen_effect.draw(self.screen)
        self.player.sprite.lasers.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_blocks.draw(self.screen)
        self.alien_manager.draw(self.screen)
        self.lives_display.draw(self.screen)
        self.score.draw(self.screen)
