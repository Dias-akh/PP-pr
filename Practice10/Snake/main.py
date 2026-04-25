import pygame
from sys import exit
from snake import Snake
from food import Food
pygame.init()

clock=pygame.time.Clock()

cell_size=20
grid_width=30
grid_height=20
screen_width=cell_size*grid_width
screen_height=cell_size*grid_height

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Snake')
font=pygame.font.SysFont('Arial',25)
sound=pygame.mixer.Sound('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Snake/sound/chew.mp3')

MOVE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_EVENT, 200)

snake = Snake(cell_size)
food=Food(cell_size,grid_width,grid_height)
score=0
level = 1
speed = 200
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==MOVE_EVENT:
            head_x, head_y = snake.body[0]
            dir_x, dir_y = snake.direction
            new_pos = (head_x + dir_x, head_y + dir_y)
            
            if new_pos[0] < 0 or new_pos[0] >= grid_width:
                screen.fill((255,0,0))
                fail_text=font.render('Game over',True,(255,255,255))
                screen.blit(fail_text,(230,185))
                pygame.display.flip()
                pygame.time.delay(2000)
                pygame.quit()
                exit()
            if new_pos[1] < 0 or new_pos[1] >= grid_height:
                screen.fill((255,0,0))
                fail_text=font.render('Game over',True,(255,255,255))
                screen.blit(fail_text,(230,185))
                pygame.display.flip()
                pygame.time.delay(2000)
                pygame.quit()
                exit()
            if new_pos in snake.body:
                screen.fill((255,0,0))
                fail_text=font.render('Game over',True,(255,255,255))
                screen.blit(fail_text,(230,185))
                pygame.display.flip()
                pygame.time.delay(2000)
                pygame.quit()
                exit()
           
            if new_pos == food.position:
                sound.play()
                snake.move(grow=True) 
                score += 1
                food.spawn(snake.body)
                if score % 3 == 0:  
                    level += 1
                    speed = max(50, speed - 20) 
                    pygame.time.set_timer(MOVE_EVENT, speed)
            else:
                snake.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0,-1))
            if event.key == pygame.K_DOWN:
                snake.change_direction((0,1))
            if event.key == pygame.K_LEFT:
                snake.change_direction((-1,0))
            if event.key == pygame.K_RIGHT:
                snake.change_direction((1,0))
    screen.fill((0,0,0))
    score_text=font.render(f"Score: {score}",True,(255,255,255))
    screen.blit(score_text,(10,10))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(level_text, (10, 40))

    snake.draw(screen)
    food.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    