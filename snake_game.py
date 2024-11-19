from constants import Dimension, Color
from snake import Snake
from food import Food

class SnakeGame:
    def __init__(self, pygame):
        self.pygame = pygame
        self.display = self.pygame.display.set_mode((Dimension.DISPLAY_WIDTH.value, Dimension.DISPLAY_HEIGHT.value)) 
        pygame.display.set_caption("Snake Game")
        self.clock = self.pygame.time.Clock()
        self.snake = Snake(self.pygame)
        self.food  = Food(self.pygame)
        self.running = True

    def handle_events(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.running = False
            if event.type == self.pygame.KEYDOWN:
                if event.key == self.pygame.K_LEFT and self.snake.direction != (Dimension.BLOCK_SIZE.value, 0):
                    self.snake.direction = (-Dimension.BLOCK_SIZE.value, 0)
                elif event.key == self.pygame.K_RIGHT and self.snake.direction != (-Dimension.BLOCK_SIZE.value, 0):
                    self.snake.direction = (Dimension.BLOCK_SIZE.value, 0)
                elif event.key == self.pygame.K_UP and self.snake.direction != (0, Dimension.BLOCK_SIZE.value):
                    self.snake.direction = (0, -Dimension.BLOCK_SIZE)
                elif event.key == self.pygame.K_DOWN and self.snake.direction != (0, -Dimension.BLOCK_SIZE.value):
                    self.snake.direction = (0, Dimension.BLOCK_SIZE.value)

    def update(self):
        self.snake.move()

        #Check collision with food
        if self.snake.body[-1] == self.food.position:
            self.snake.grow()
            self.food.position = self.food.generate_position()

        #Check collistion with walls or itself
        if self.snake.check_collision():
            self.running = False

    def draw(self):
        self.display.fill(Color.BLUE.value)
        self.snake.draw(self.display)
        self.food.draw(self.display)
        self.pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)
        self.pygame.quit()

    
