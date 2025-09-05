from player import Player
import pygame
import screen_size
import obstacle

# Represents the game logic.
class Game:
    NUM_OBSTACLES = 4

    def __init__(self, screen: pygame.display):
        # Initializing the screen dependency 
        self.screen = screen
        
        # Initializing the player instance variable
        player_sprite = Player((screen_size.SCREEN_WIDTH / 2, screen_size.SCREEN_HEIGHT))
        self.player = pygame.sprite.GroupSingle(player_sprite)

        # Initializing obstacles
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_x_positions = [num * (screen_size.SCREEN_WIDTH / self.NUM_OBSTACLES) for num in range(self.NUM_OBSTACLES)]
        self.create_multiple_obstacles(self.obstacle_x_positions, x_start = 0, y_start = 480)

    # TODO: decouple obstacle from game
    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col == 'x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size, "red", x, y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self, offset, x_start, y_start):
        for offset_x in offset:
            self.create_obstacle(x_start, y_start, offset_x)


    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(self.screen)
        self.player.draw(self.screen)
        self.blocks.draw(self.screen)

