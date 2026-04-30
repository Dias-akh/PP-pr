import pygame
from datetime import datetime
from sys import exit

pygame.init()

W, H = 600, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_caption('Paint')

canvas = pygame.Surface((600, 600))
canvas.fill('White')

image = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Paint/eraser-icon-16.png')
image = pygame.transform.scale(image, (40, 40))

surface = pygame.Surface((600, 115))
surface.fill('Black')

current_color = 'Black'
current_size = 2
mode = 'pen' 
drawing = False
start_pos = None
last_pos = None
text_mode_active = False
text_input = ''
text_pos = None
font = pygame.font.SysFont(None, 36)

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Gray']

def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))
    new_color = pygame.Color(new_color)
    if target_color == new_color:
        return
    stack = [(x, y)]
    w, h = surface.get_size()
    visited = set()
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        if cx < 0 or cx >= w or cy < 0 or cy >= h:
            continue
        if surface.get_at((cx, cy)) != target_color:
            continue
        visited.add((cx, cy))
        surface.set_at((cx, cy), new_color)
        stack.append((cx + 1, cy))
        stack.append((cx - 1, cy))
        stack.append((cx, cy + 1))
        stack.append((cx, cy - 1))

while True:
    screen.fill('White')
    screen.blit(canvas, (0, 0)) 
    screen.blit(surface, (0, 0)) 
    
    pygame.draw.rect(screen, 'White', (10, 20, 40, 40))
    pygame.draw.rect(screen, 'Black', (15, 25, 30, 30), 2)
    pygame.draw.rect(screen, 'White', (55, 20, 40, 40))
    pygame.draw.circle(screen, 'Black', (75, 40), 15, 2)
    pygame.draw.rect(screen, 'White', (100, 20, 40, 40))
    pygame.draw.line(screen, 'Black', (110, 50), (130, 30), 2)
    pygame.draw.rect(screen, 'White', (145, 20, 40, 40))
    screen.blit(image, (145, 20))
    pygame.draw.rect(screen, 'White', (190, 20, 40, 40))
    pygame.draw.rect(screen, 'Black', (200, 30, 20, 20), 2)
    pygame.draw.rect(screen, 'White', (235, 20, 40, 40))
    pygame.draw.polygon(screen, 'Black', [(245, 30), (245, 50), (265, 50)], 2)
    pygame.draw.rect(screen, 'White', (280, 20, 40, 40))
    pygame.draw.polygon(screen, 'Black', [(300, 30), (290, 50), (310, 50)], 2)
    pygame.draw.rect(screen, 'White', (325, 20, 40, 40))
    pygame.draw.polygon(screen, 'Black', [(345, 25), (355, 40), (345, 55), (335, 40)], 2)
    pygame.draw.rect(screen, 'White', (370, 20, 40, 40))
    pygame.draw.line(screen, 'Black', (380, 50), (400, 30), 2)
    pygame.draw.rect(screen, 'Blue', (520, 15, 30, 30))
    pygame.draw.rect(screen, 'Yellow', (555, 15, 30, 30))
    pygame.draw.rect(screen, 'Red', (520, 55, 30, 30))
    pygame.draw.rect(screen, 'Green', (555, 55, 30, 30))
    pygame.draw.rect(screen, 'White', (10, 65, 40, 40))
    pygame.draw.circle(screen, 'Black', (30, 85), 2) 
    pygame.draw.rect(screen, 'White', (55, 65, 40, 40))
    pygame.draw.circle(screen, 'Black', (75, 85), 5)
    pygame.draw.rect(screen, 'White', (100, 65, 40, 40))
    pygame.draw.circle(screen, 'Black', (120, 85), 10)
    pygame.draw.rect(screen, 'White', (415, 20, 40, 40))
    pygame.draw.rect(screen, current_color, (420, 25, 30, 30))
    pygame.draw.rect(screen, 'White', (460, 20, 40, 40))
    pygame.draw.rect(screen, 'Black', (463, 23, 34, 34), 2)
    text_surface = font.render('T', True, 'Black')
    screen.blit(text_surface, (472, 28))

    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: current_size = 2
            elif event.key == pygame.K_2: current_size = 5
            elif event.key == pygame.K_3: current_size = 10
            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_META:
                timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                filename = f'canvas_{timestamp}.png'
                pygame.image.save(canvas, filename)
                print(f'Saved: {filename}')
            elif text_mode_active:
                if event.key == pygame.K_RETURN:

                    text_surface = font.render(text_input, True, current_color)
                    canvas.blit(text_surface, text_pos)
                    text_mode_active = False
                    text_input = ''
                    text_pos = None
                elif event.key == pygame.K_ESCAPE:
                    text_mode_active = False
                    text_input = ''
                    text_pos = None
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if my < 115:

                if 20 <= my <= 60:
                    if 10 <= mx <= 50: mode = 'rect'
                    elif 55 <= mx <= 95: mode = 'circle'
                    elif 100 <= mx <= 140: mode = 'pen'
                    elif 145 <= mx <= 185: mode = 'eraser'
                    elif 190 <= mx <= 230: mode = 'square'
                    elif 235 <= mx <= 275: mode = 'r_triangle'
                    elif 280 <= mx <= 320: mode = 'e_triangle'
                    elif 325 <= mx <= 365: mode = 'rhombus'
                    elif 370 <= mx <= 410: mode = 'line'
                    elif 415 <= mx <= 455: mode = 'fill'
                    elif 460 <= mx <= 500: mode = 'text'
    

                if 520 <= mx <= 550 and 15 <= my <= 45: current_color = 'Blue'
                elif 555 <= mx <= 585 and 15 <= my <= 45: current_color = 'Yellow'
                elif 520 <= mx <= 550 and 55 <= my <= 85: current_color = 'Red'
                elif 555 <= mx <= 585 and 55 <= my <= 85: current_color = 'Green'
    

                if 10 <= mx <= 50 and 65 <= my <= 105: current_size = 2
                elif 55 <= mx <= 95 and 65 <= my <= 105: current_size = 5
                elif 100 <= mx <= 140 and 65 <= my <= 105: current_size = 10
            else:
                if mode == 'fill':
                    flood_fill(canvas, mx, my, current_color)
                elif mode == 'text':
                    text_mode_active = True
                    text_input = ''
                    text_pos = (mx, my)
                else:
                    drawing = True
                    start_pos = (mx, my)
                    last_pos = (mx, my)

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing and start_pos:
                if mode == 'rect':
                    width = mouse_pos[0] - start_pos[0]
                    height = mouse_pos[1] - start_pos[1]
                    pygame.draw.rect(canvas, current_color, (start_pos[0], start_pos[1], width, height), current_size)
                elif mode == 'circle':
                    radius = int(((mouse_pos[0] - start_pos[0])**2 + (mouse_pos[1] - start_pos[1])**2)**0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, current_size)
                elif mode == 'square':
                    side = mouse_pos[0] - start_pos[0] 
                    pygame.draw.rect(canvas, current_color, (start_pos[0], start_pos[1], side, side), current_size)
                elif mode == 'r_triangle':
                    points = [start_pos, (start_pos[0], mouse_pos[1]), mouse_pos]
                    pygame.draw.polygon(canvas, current_color, points, current_size)
                elif mode == 'rhombus':
                    mid_x = (start_pos[0] + mouse_pos[0]) // 2
                    mid_y = (start_pos[1] + mouse_pos[1]) // 2
                    points = [(mid_x, start_pos[1]), (mouse_pos[0], mid_y), (mid_x, mouse_pos[1]), (start_pos[0], mid_y)]
                    pygame.draw.polygon(canvas, current_color, points, current_size)
                elif mode == 'e_triangle':
                    mid_x = (start_pos[0] + mouse_pos[0]) // 2
                    points = [(mid_x, start_pos[1]), (start_pos[0], mouse_pos[1]), (mouse_pos[0], mouse_pos[1])]
                    pygame.draw.polygon(canvas, current_color, points, current_size)
                elif mode == 'line':
                    pygame.draw.line(canvas, current_color, start_pos, mouse_pos, current_size)
            drawing = False
            start_pos = None

    if drawing and start_pos and mouse_pos[1] > 115:
        if mode == 'pen':
            pygame.draw.line(canvas, current_color, last_pos, mouse_pos, current_size)
            last_pos = mouse_pos
        elif mode == 'eraser':
            pygame.draw.line(canvas, 'White', last_pos, mouse_pos, current_size)
            last_pos = mouse_pos
        elif mode == 'rect':
            width = mouse_pos[0] - start_pos[0]
            height = mouse_pos[1] - start_pos[1]
            pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], width, height), current_size)
        elif mode == 'circle':
            radius = int(((mouse_pos[0] - start_pos[0])**2 + (mouse_pos[1] - start_pos[1])**2)**0.5)
            pygame.draw.circle(screen, current_color, start_pos, radius, current_size)
        elif mode == 'square':
            side = mouse_pos[0] - start_pos[0] 
            pygame.draw.rect(screen, current_color, (start_pos[0], start_pos[1], side, side), current_size)
        elif mode == 'r_triangle':
            points = [start_pos, (start_pos[0], mouse_pos[1]), mouse_pos]
            pygame.draw.polygon(screen, current_color, points, current_size)
        elif mode == 'rhombus':
            mid_x = (start_pos[0] + mouse_pos[0]) // 2
            mid_y = (start_pos[1] + mouse_pos[1]) // 2
            points = [(mid_x, start_pos[1]), (mouse_pos[0], mid_y), (mid_x, mouse_pos[1]), (start_pos[0], mid_y)]
            pygame.draw.polygon(screen, current_color, points, current_size)
        elif mode == 'e_triangle':
            mid_x = (start_pos[0] + mouse_pos[0]) // 2
            points = [(mid_x, start_pos[1]), (start_pos[0], mouse_pos[1]), (mouse_pos[0], mouse_pos[1])]
            pygame.draw.polygon(screen, current_color, points, current_size)
        elif mode == 'line':
            pygame.draw.line(screen, current_color, start_pos, mouse_pos, current_size)
    if text_mode_active and text_pos:
        preview = font.render(text_input + '|', True, current_color)
        screen.blit(preview, text_pos)
    pygame.display.flip()
    clock.tick(60)