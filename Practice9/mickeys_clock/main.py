import pygame
from sys import exit
from clock import Clock

pygame.init()
screen = pygame.display.set_mode((700, 600))

image_surface = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice9/mickeys_clock/images/mickeyclock.jpeg')
image_surface = pygame.transform.scale(image_surface, (700, 600))

clock_obj = Clock()
tick = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(image_surface, (0, 0))
    clock_obj.draw(screen)
    tick.tick(60)
    pygame.display.flip()