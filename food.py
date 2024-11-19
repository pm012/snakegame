from constants import Dimension, Color
import random


class Food:
    def __init__(self, pygame):
        self.position = self.generate_position()
        self.pygame = pygame

    def generate_position(self) -> list:
        x = round(random.randrange(0, Dimension.DISPLAY_WIDTH.value - Dimension.BLOCK_SIZE.value) / 10.0) * 10.0
        y = round(random.randrange(0, Dimension.DISPLAY_HEIGHT.value - Dimension.BLOCK_SIZE.value) / 10.0) * 10.0
        return [x, y]
    
    def draw(self, surface):
        self.pygame.draw.rect(surface, Color.GREEN.value, [self.position[0], self.position[1], Dimension.BLOCK_SIZE.value, Dimension.BLOCK_SIZE.value])


