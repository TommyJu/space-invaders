from player import Player
import pygame

# Represents the game logic.
class Game:
    def __init__(self, screen, screen_size):
        self._screen = screen
        self._width, self._height = screen_size
        
        player_sprite = Player((self._width / 2, self._height / 2))
        self._player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self._player.draw(self._screen)