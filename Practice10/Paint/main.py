import pygame
from sys import exit

pygame.init()

W, H = 600, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_caption('Paint')

canvas = pygame.Surface((600, 600))
canvas.fill('White')


image = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Paint/eraser-icon-16.png')
image = pygame.transform.scale(image, (50, 50))

surface = pygame.Surface((600, 70))
surface.fill('Black')


current_color = 'Black'
mode = 'pen' 
drawing = False
start_pos = None

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Black']

while True:
    screen.fill('White')
    screen.blit(canvas, (0, 0)) 
    screen.blit(surface, (0, 0)) 
    
    pygame.draw.rect(screen, 'White', (10, 10, 50, 50))
    pygame.draw.rect(screen, 'Black', (15, 15, 40, 40), 2)
    
    pygame.draw.rect(screen, 'White', (70, 10, 50, 50))
    pygame.draw.circle(screen, 'Black', (95, 35), 20, 2)
    
    pygame.draw.rect(screen, 'White', (130, 10, 50, 50))
    pygame.draw.line(screen, 'Black', (140, 50), (170, 20), 3)
    
    pygame.draw.rect(screen, 'White', (190, 10, 50, 50))
    screen.blit(image, (190, 10))
    
    for i, color in enumerate(colors):
        rect_x = W - 60 - (i * 45)
        pygame.draw.rect(screen, color, (rect_x, 15, 35, 35))
        if current_color == color:
            pygame.draw.rect(screen, 'White', (rect_x, 15, 35, 35), 2)

    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse_pos[1] < 70:
                if 10 <= mouse_pos[0] <= 60: mode = 'rect'
                elif 70 <= mouse_pos[0] <= 120: mode = 'circle'
                elif 130 <= mouse_pos[0] <= 180: mode = 'pen'
                elif 190 <= mouse_pos[0] <= 240: mode = 'eraser'
                for i, color in enumerate(colors):
                    rect_x = W - 60 - (i * 45)
                    if rect_x <= mouse_pos[0] <= rect_x + 35:
                        current_color = color
            else:
                drawing = True
                start_pos = mouse_pos       
        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                if mode == 'rect':
                    width = mouse_pos[0] - start_pos[0]
                    height = mouse_pos[1] - start_pos[1]
                    pygame.draw.rect(canvas, current_color, (start_pos[0], start_pos[1], width, height), 2)
                elif mode == 'circle':
                    radius = int(((mouse_pos[0] - start_pos[0])**2 + (mouse_pos[1] - start_pos[1])**2)**0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)
            drawing = False
            start_pos = None


    if drawing and start_pos and mouse_pos[1] > 70:
        if mode == 'pen':
            pygame.draw.circle(canvas, current_color, mouse_pos, 3)
        elif mode == 'eraser':

            pygame.draw.circle(canvas, 'White', mouse_pos, 20)
        elif mode == 'rect':
            width = mouse_pos[0] - start_pos[0]
            height = mouse_pos[1] - start_pos[1]
            pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], width, height), 2)
        elif mode == 'circle':
            radius = int(((mouse_pos[0] - start_pos[0])**2 + (mouse_pos[1] - start_pos[1])**2)**0.5)
            pygame.draw.circle(screen, current_color, start_pos, radius, 2)

    pygame.display.flip()
    clock.tick(60)