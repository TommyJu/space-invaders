import pygame
from constants import alien_constants
from random import randint, choice
import extra_alien
import alien

# Represents the state of the aliens during the game
class AlienManager:
    def __init__(self):
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        self.aliens_x_direction = 1
        self.aliens.add(alien.alien_setup())
        # Extra alien that spawns in periodically
        self.extra_alien = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(alien_constants.EXTRA_ALIEN_SPAWN_TIME_MIN,
                                       alien_constants.EXTRA_ALIEN_SPAWN_TIME_MAX)


    # Updates the horizontal movement direction of all aliens (extra alien not included)
    def set_aliens_x_direction(self, new_direction: int):
        self.aliens_x_direction = new_direction

    
    # Selects a random alien to shoot a laser at the player
    def alien_shoot(self):
        self.alien_lasers.add(alien.create_laser(self.aliens))


    # Updates the spawn timer for the extra alien
    def update_extra_alien_timer(self):
        self.extra_spawn_time -= 1
        if self.extra_spawn_time <= 0:
            start = choice(["left", "right"])
            self.extra_alien.add(extra_alien.Extra(start))
            self.extra_spawn_time = randint(alien_constants.EXTRA_ALIEN_SPAWN_TIME_MIN,
                                            alien_constants.EXTRA_ALIEN_SPAWN_TIME_MAX)


    # Updates all alien state
    def update(self):
        self.aliens.update(self.aliens_x_direction)
        self.alien_lasers.update()
        self.update_extra_alien_timer()
        if self.extra_alien:
            self.extra_alien.update()


    # Draws all alien sprites and lasers to the screen
    def draw(self, screen):
        self.aliens.draw(screen)
        self.alien_lasers.draw(screen)
        self.extra_alien.draw(screen)