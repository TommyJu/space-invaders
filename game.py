from player import Player
import pygame

# Represents the game logic.
class Game:
    def __init__(self, screen: pygame.display, screen_size: tuple[int, int]):
        # Initializing the screen dependency 
        self.screen = screen
        self.width, self.height = screen_size
        
        # Initializing the player instance variable
        player_sprite = Player((self.width / 2, self.height / 2))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(self.screen)

