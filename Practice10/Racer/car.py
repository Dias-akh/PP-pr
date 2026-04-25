import pygame
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__() 
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x = x    
        self.rect.y = y
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx   
        self.rect.y += dy 

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def move(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy
