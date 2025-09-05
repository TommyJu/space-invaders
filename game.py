from player import Player
import pygame
from constants import screen_size, alien_constants
import obstacle
import alien
import extra_alien
from random import randint, choice
import collision

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
        self.alien_lasers = pygame.sprite.Group()
        self.aliens.add(alien.alien_setup())
        self.aliens_x_direction = self.DEFAULT_ALIEN_X_DIRECTION
        
        # Initializing extra alien
        self.extra_alien = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(alien_constants.EXTRA_ALIEN_SPAWN_TIME_MIN, alien_constants.EXTRA_ALIEN_SPAWN_TIME_MAX)

    # Determines when to spawn the extra alien
    def extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            extra_alien_x_start = choice(["left", "right"])
            self.extra_alien.add(extra_alien.Extra(extra_alien_x_start))
            self.extra_spawn_time = randint(alien_constants.EXTRA_ALIEN_SPAWN_TIME_MIN, alien_constants.EXTRA_ALIEN_SPAWN_TIME_MAX)

    
    # Event callback for the ALIEN_SHOOT event timer
    def alien_shoot(self):
         self.alien_lasers.add(alien.create_laser(self.aliens))


    def run(self):
        # Updating game state
        self.player.update()
        self.aliens.update(self.aliens_x_direction)
        self.alien_lasers.update()
        self.extra_alien_timer()
        self.extra_alien.update()
        # Collision checks
        self.aliens_x_direction = collision.alien_screen_collision(self.aliens, self.aliens_x_direction)
        collision.alien_laser_collision_checks(self.alien_lasers, self.player, self.obstacle_blocks)
        collision.player_laser_collision_checks(self.player, self.aliens, self.obstacle_blocks)
        # Drawing sprites to the screen
        self.player.sprite.lasers.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_blocks.draw(self.screen)
        self.aliens.draw(self.screen)
        self.alien_lasers.draw(self.screen)
        self.extra_alien.draw(self.screen)