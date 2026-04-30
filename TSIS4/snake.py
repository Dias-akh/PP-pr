import pygame

class Snake:
    def __init__(self, cell_size, color=(0, 255, 0)):
        self.cell_size = cell_size
        self.body = [(10, 10), (9, 10), (8, 10)]
        self.direction = (1, 0)
        self.color = color

    def move(self, grow=False):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.body.insert(0, new_head)
        if not grow:
            self.body.pop()

    def shorten(self, count):
        for _ in range(count):
            if len(self.body) > 0:
                self.body.pop()

    def change_direction(self, new_dir):
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir

    def draw(self, screen):
        for i, pos in enumerate(self.body):
            color = self.color if i == 0 else (max(0, self.color[0]-50), max(0, self.color[1]-50), max(0, self.color[2]-50))
            pygame.draw.rect(screen, color, (pos[0]*self.cell_size, pos[1]*self.cell_size, self.cell_size-1, self.cell_size-1))