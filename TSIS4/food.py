import pygame
import random

class GameObject:
    def __init__(self, grid_w, grid_h, cell_size):
        self.grid_w, self.grid_h, self.cell_size = grid_w, grid_h, cell_size
        self.pos = (0, 0)

    def spawn(self, exclude):
        while True:
            self.pos = (random.randint(0, self.grid_w-1), random.randint(0, self.grid_h-1))
            if self.pos not in exclude: 
                break

class Food(GameObject):
    def __init__(self, grid_w, grid_h, cell_size):
        super().__init__(grid_w, grid_h, cell_size)
        self.timer = pygame.time.get_ticks() + 8000 
        self.is_poison = False
        self.weight = 1
        self.spawn([]) 

    def spawn(self, exclude):
        super().spawn(exclude)
        self.is_poison = random.random() < 0.15 
        self.weight = 0 if self.is_poison else random.choice([1, 3, 5])
        self.timer = pygame.time.get_ticks() + 8000 

    def draw(self, screen):
        color = (150, 0, 0) if self.is_poison else (255, 255, 0)
        pygame.draw.rect(screen, color, (self.pos[0] * self.cell_size, self.pos[1] * self.cell_size, self.cell_size - 1, self.cell_size - 1))

class PowerUp(GameObject):
    def __init__(self, grid_w, grid_h, cell_size):
        super().__init__(grid_w, grid_h, cell_size)
        self.pos = (-1, -1)
        self.timer = 0
        self.type = "speed"

    def spawn(self, exclude):
        super().spawn(exclude)
        self.type = random.choice(["speed", "slow", "shield"]) 
        self.timer = pygame.time.get_ticks() + 8000

    def draw(self, screen):
        if self.pos != (-1, -1):
            pygame.draw.circle(screen, (0, 0, 255), (self.pos[0] * self.cell_size + 10, self.pos[1] * self.cell_size + 10), 8)