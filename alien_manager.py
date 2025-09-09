import pygame
from constants import alien_constants
from random import randint, choice
import extra_alien
import alien
from events import ALIEN_LASER_EVENT
from laser import Laser

# Represents the state of the aliens during the game
class AlienManager:
    def __init__(self):
        self.aliens = pygame.sprite.Group()
        self.alien_lasers = pygame.sprite.Group()
        
        # Variables that change with difficulty
        self.aliens_x_direction = alien_constants.SPEED_EASY
        self.aliens_color = alien_constants.COLOR_EASY
        self.alien_laser_timer = pygame.time.set_timer(ALIEN_LASER_EVENT, alien_constants.LASER_COOLDOWN_EASY)

        # Extra alien that spawns in periodically
        self.extra_alien = pygame.sprite.GroupSingle()
        self.extra_spawn_time = randint(alien_constants.EXTRA_ALIEN_SPAWN_TIME_MIN,
                                       alien_constants.EXTRA_ALIEN_SPAWN_TIME_MAX)
        self.alien_setup()

    def change_difficulty_medium(self):
        self.aliens_x_direction = alien_constants.SPEED_MEDIUM
        self.aliens_color = alien_constants.COLOR_MEDIUM
        self.alien_laser_timer = pygame.time.set_timer(ALIEN_LASER_EVENT, alien_constants.LASER_COOLDOWN_MEDIUM)

    def change_difficulty_hard(self):
        self.aliens_x_direction = alien_constants.SPEED_HARD
        self.aliens_color = alien_constants.COLOR_HARD
        self.alien_laser_timer = pygame.time.set_timer(ALIEN_LASER_EVENT, alien_constants.LASER_COOLDOWN_HARD)

    # Sets up the aliens like bowling pins
    def alien_setup(self):
        self.alien_lasers.empty()
        for row in range(alien_constants.ROWS):
            for column in range(alien_constants.COLUMNS):
                x = column * alien_constants.X_OFFSET
                y = (row + 1) * alien_constants.Y_OFFSET
                alien_color = self.aliens_color
                alien_sprite = alien.Alien(alien_color, x, y)
                self.aliens.add(alien_sprite)


    # Updates the horizontal movement direction of all aliens (extra alien not included)
    def flip_aliens_x_direction(self):
        self.aliens_x_direction = -self.aliens_x_direction

    def create_laser(self):
        if self.aliens:
            random_alien = choice(self.aliens.sprites())
            return Laser(random_alien.rect.center, alien_constants.LASER_SPEED, alien_constants.LASER_COLOR)
    
    # Selects a random alien to shoot a laser at the player
    def alien_shoot(self):
        if self.aliens:
            self.alien_lasers.add(self.create_laser())

    def shift_aliens_down(self):
        for alien in self.aliens:
            alien.rect.y += alien_constants.COLLISION_Y_SHIFT


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