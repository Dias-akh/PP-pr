import pygame
from ball import Ball
from sys import exit

pygame.init()

Width=600
Height=600

clock=pygame.time.Clock()
screen=pygame.display.set_mode((Width,Height))
pygame.display.set_caption('Ball game')
ball=Ball(Width//2,Height//2)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                ball.move(0,-20,Width,Height)
            if event.key==pygame.K_DOWN:
                ball.move(0,+20,Width,Height)
            if event.key==pygame.K_LEFT:
                ball.move(-20,0,Width,Height)
            if event.key==pygame.K_RIGHT:
                ball.move(+20,0,Width,Height)
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255, 0, 0),(ball.x, ball.y), ball.radius)
    pygame.display.flip()
    clock.tick(60)



