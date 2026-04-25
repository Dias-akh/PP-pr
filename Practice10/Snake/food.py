import pygame
import random

YELLOW = (255, 255, 0)
class Food:
    def __init__(self,cell_size,grid_width,grid_height):
        self.cell_size=cell_size
        self.grid_width=grid_width
        self.grid_height=grid_height
        self.spawn(snake_body=[])
    
    def spawn(self, snake_body):
        while True:
            x = random.randint(0, self.grid_width - 1)
            y = random.randint(0, self.grid_height - 1)
            if (x, y) not in snake_body:
                self.position = (x, y)
                break
    def draw(self, screen):
        col, row = self.position
        pygame.draw.rect(screen, YELLOW, (
            col * self.cell_size,
            row * self.cell_size,
            self.cell_size - 1,
            self.cell_size - 1
        ))
