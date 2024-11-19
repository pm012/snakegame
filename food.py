from constants import Dimension, Color
import random


class Food:
    def __init__(self, pygame):
        self.position = self.generate_position()
        self.pygame = pygame

    def generate_position(self) -> list:
        x = round(random.range(0, Dimension.DISPLAY_WIDTH - Dimension.BLOCK_SIZE) / 10.0) * 10.0
        y = round(random.randrange(0, Dimension.DISPLAY_HEIGHT - Dimension.BLOCK_SIZE) / 10.0) * 10.0
        return [x, y]
    
    def draw(self, surface):
        self.pygame.draw.rect(surface, Color.GREEN, [self.position[0], self.position[1], Dimension.BLOCK_SIZE, Dimension.BLOCK_SIZE])


