import pygame
from sys import exit
from car import Car
from car import Coin
from random import randint , choice
pygame.init()

width=500
height=700
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Racer game')

image_object1=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/Road.png')
image_object1=pygame.transform.scale(image_object1,(500,350))
image_object2=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/Road.png')
image_object2=pygame.transform.scale(image_object2,(500,350))
image_object3=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/Road.png')
image_object3=pygame.transform.scale(image_object3,(500,350))

font_object=pygame.font.SysFont('Arial',20)

clock=pygame.time.Clock()

car_image = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/car1.png')
car_image = pygame.transform.scale(car_image, (100, 150))
car = Car(170, 500, car_image)

lines = [85, 175, 255, 340]
coin_image=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/coin.png')
coin_image=pygame.transform.scale(coin_image,(65,65))
coin = Coin(choice(lines), -80, coin_image)

road1_y = 0
road2_y = 350    
road3_y = -350   
road_speed = 3


coin_y=0
speed_coin=3
score=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if car.rect.x >= 170:
                    car.move(-85, 0)
            if event.key == pygame.K_RIGHT:
                if car.rect.x<=323:
                    car.move(85, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
           print(pygame.mouse.get_pos())
    

    road1_y += road_speed
    road2_y += road_speed
    road3_y += road_speed  
    if road1_y >= 700:
        road1_y = -350
    if road2_y >= 700:
        road2_y = -350
    if road3_y >= 700:
        road3_y = -350
    screen.blit(image_object1,(0,road1_y))
    screen.blit(image_object2,(0,road2_y))
    screen.blit(image_object3, (0, road3_y))
    car.draw(screen)

    coin.move(0, road_speed)
    if coin.rect.y >= 700:  
        coin.rect.x = choice(lines)  

        coin.rect.y = -80

    if pygame.sprite.collide_rect(car, coin):
        score += 5
        coin.rect.x = choice(lines)
        coin.rect.y = -80
    coin.draw(screen)

    score_text=font_object.render(f"Score {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    
    pygame.display.flip() 
    clock.tick(60) 
        
        
