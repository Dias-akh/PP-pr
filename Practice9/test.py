import pygame
from sys import exit

pygame.init()
screen=pygame.display.set_mode((600,600))
clock=pygame.time.Clock()
screen.fill('Blue')
image_object=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice9/mickeys_clock/images/mickeyclock.jpeg')
image_object=pygame.transform.scale(image_object,(600,600))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(image_object,(0,0))
    pygame.display.update()
    clock.tick(60)


    
    
