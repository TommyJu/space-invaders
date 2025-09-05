import pygame
from constants import obstacle_constants
from constants import screen_size

class Block(pygame.sprite.Sprite):

    def __init__(self, size, color, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = (x, y))

# Returns a list of block sprites that make up an entire obstacle
def create_obstacle(x_start, y_start, offset_x):
    blocks = list()
    for row_index, row in enumerate(obstacle_constants.SHAPE):
        for col_index, col in enumerate(row):
            if col == 'x':
                x = x_start + offset_x + (col_index * obstacle_constants.BLOCK_SIZE)
                y = y_start + (row_index * obstacle_constants.BLOCK_SIZE)
                blocks.append(Block(obstacle_constants.BLOCK_SIZE, obstacle_constants.COLOR, x, y))
    
    return blocks


# Returns a list of obstacles
def create_multiple_obstacles():
    obstacles = list()
    obstacle_x_offsets = [num * (screen_size.SCREEN_WIDTH / obstacle_constants.NUM_OBSTACLES) for num in range(obstacle_constants.NUM_OBSTACLES)]
    for x_offset in obstacle_x_offsets:
        obstacles.append(create_obstacle(obstacle_constants.OBSTACLES_X_POSITION, obstacle_constants.OBSTACLES_Y_POSITION, x_offset))
    
    return obstacles
