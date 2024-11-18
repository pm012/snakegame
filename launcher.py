import pygame
from snake_game import SnakeGame



# Launch the game
if __name__ == "__main__":
    pygame.init()
    game = SnakeGame(pygame)
    game.run