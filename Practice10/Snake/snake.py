import pygame

Green=(0,255,0)
LGreen=(0,150,0)

class Snake:
    def __init__(self, cell_size):
        self.cell_size=cell_size
        self.body=[(10,10),(9,10),(8,10)]
        self.direction=(1,0)

    def move(self,grow=False):
        head_x,head_y=self.body[0]
        dir_x,dir_y=self.direction
        new_head=(head_x+dir_x,head_y+dir_y)

        self.body.insert(0,new_head)

        if not grow:
            self.body.pop()
    


    def change_direction(self,new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction

    def draw(self, screen):
        for i, (col, row) in enumerate(self.body):
            if i == 0:
                color = Green 
            else:
                color = LGreen
            pygame.draw.rect(screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size - 1, self.cell_size - 1))

