import pygame
import random

class Obstacles:
    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.blocks = []

    def generate(self, level, exclude, grid_w, grid_h):
        self.blocks = []
        if level >= 3:
            for _ in range(level * 2):
                while True:
                    pos = (random.randint(0, grid_w-1), random.randint(0, grid_h-1))
                    if pos not in exclude:
                        self.blocks.append(pos)
                        break

    def draw(self, screen):
        for b in self.blocks:
            pygame.draw.rect(screen, (120, 120, 120), (b[0]*self.cell_size, b[1]*self.cell_size, self.cell_size-1, self.cell_size-1))