import pygame
class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__() 
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x = x    
        self.rect.y = y
        self.rect.inflate_ip(-30, -30)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx   
        self.rect.y += dy 

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.inflate_ip(-30, -30)

    def move(self, speed):
        self.rect.y += speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rect.inflate_ip(-30, -30)
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def move(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy

class Obst(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rect.inflate_ip(-30, -30)
    def draw(self,screen):
        screen.blit(self.image, self.rect)
    def move(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy

class Oil(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rect.inflate_ip(-30, -30)
    def draw(self,screen):
        screen.blit(self.image, self.rect)
    def move(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy

class Bump(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rect.inflate_ip(-30, -30)
    def draw(self,screen):
        screen.blit(self.image, self.rect)
    def move(self,dx,dy):
        self.rect.x+=dx
        self.rect.y+=dy

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, image, ptype):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.ptype = ptype  # 'nitro', 'shield', 'repair'

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


