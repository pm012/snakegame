from constants import Dimension
class Snake:
    def __init__(self):
        self.body = [[Dimension.DISPLAY_WIDTH//2, Dimension.DISPLAY_HEIGHT//2]]
        self.direction = (0, 0)
        self.length = 1

    def move(self):
        head_x, head_y = self.body[-1]
        delta_x, delta_y = self.direction
        new_head = [head_x + delta_x, head_y + delta_y]
        self.body.append(new_head)


        if len(self.body) > self.length:
            self.body.pop(0)

    