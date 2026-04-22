class Ball():
    def __init__(self,x,y):
        self.radius=25
        self.x=x
        self.y=y
    
    def move(self,dx,dy,screen_width,screen_height):
        new_x=self.x+dx
        new_y=self.y+dy

        if self.radius<=new_x<=screen_width-self.radius:
            self.x=new_x
        if self.radius<=new_y<=screen_height-self.radius:
            self.y=new_y


