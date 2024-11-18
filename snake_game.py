from constants import Dimension

class SnakeGame:
    def __init__(self, pygame):
        self.pygame = pygame
        self.display = self.pygame.display.set_mode((Dimension.DISPLAY_WIDTH, Dimension.DISPLAY_HEIGHT)) 
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.clock()
        self.snake = Snake()