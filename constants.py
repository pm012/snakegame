from enum import Enum

class Color(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

class Dimension(Enum):
    DISPLAY_WIDTH = 600
    DISPLAY_HEIGHT = 400
    BLOCK_SIZE = 10
    SNAKE_SPEED = 0.1
