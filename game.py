from player import Player
import pygame
import screen_size

# Represents the game logic.
class Game:
    def __init__(self, screen: pygame.display):
        # Initializing the screen dependency 
        self.screen = screen
        
        # Initializing the player instance variable
        player_sprite = Player((screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(self.screen)
        self.player.draw(self.screen)

