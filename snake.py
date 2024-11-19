from constants import Dimension, Color
class Snake:
    def __init__(self, pygame):
        self.body = [[Dimension.DISPLAY_WIDTH//2, Dimension.DISPLAY_HEIGHT//2]]
        self.direction = (0, 0)
        self.length = 1
        self.pygame = pygame

    def move(self):
        head_x, head_y = self.body[-1]
        delta_x, delta_y = self.direction
        new_head = [head_x + delta_x, head_y + delta_y]
        self.body.append(new_head)


        if len(self.body) > self.length:
            self.body.pop(0)

    def grow(self):
        self.length +=1

    def check_collision(self):
        head = self.body[-1]
        if head in self.body[::-1]: #Collides itself
            return True
        if (
            head[0] < 0 or head[0] >= Dimension.DISPLAY_WIDTH or
            head[1] < 0 or head[1] >= Dimension.DISPLAY_HEIGHT
        ): #Collides with walls
            return True
        return False
    
    def draw(self, surface):
        for segment in self.body:
            self.pygame.draw.rect(surface, Color.BLACK, [segment[0], segment[1], Dimension.BLOCK_SIZE, Dimension.BLOCK_SIZE])
            

    