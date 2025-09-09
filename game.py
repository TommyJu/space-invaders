from player import Player
import pygame
from constants import screen_size
import obstacle
import collision
import alien_manager
import lives_display
import score
import screen_effect
from audio_manager import AudioManager


# Represents the game logic.
class Game:
    def __init__(self, screen: pygame.display):
        self.screen = screen
        self.screen_effect = screen_effect.ScreenEffect()
        
        player_sprite = Player((screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT))
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.obstacle_blocks = pygame.sprite.Group()
        self.obstacle_blocks.add(obstacle.create_multiple_obstacles())

        self.alien_manager = alien_manager.AlienManager()

        self.lives_display = lives_display.LivesDisplay(self.player)

        self.score = score.Score()

        
        # Background music
        AudioManager.play_background_music()

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
