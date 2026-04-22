import pygame
import datetime
import math


class Clock:
    def __init__(self):
        self.cx = 350
        self.cy = 300

    def draw(self, surface):
        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute
        hours = now.hour % 12  


        sec_angle = math.radians(seconds * 6 - 90)
        min_angle = math.radians(minutes * 6 + seconds * 0.1 - 90)
        hour_angle = math.radians(hours * 30 + minutes * 0.5 - 90)

        
        sec_len = 160
        min_len = 130
        hour_len = 90   

        
        sec_end = (
            self.cx + int(math.cos(sec_angle) * sec_len),
            self.cy + int(math.sin(sec_angle) * sec_len)
        )
        min_end = (
            self.cx + int(math.cos(min_angle) * min_len),
            self.cy + int(math.sin(min_angle) * min_len)
        )
        hour_end = (
            self.cx + int(math.cos(hour_angle) * hour_len),
            self.cy + int(math.sin(hour_angle) * hour_len)
        )

        
        pygame.draw.line(surface, (30, 30, 30), (self.cx, self.cy), hour_end, 10)  
        pygame.draw.line(surface, (30, 30, 30), (self.cx, self.cy), min_end, 6)   
        pygame.draw.line(surface, ('Blue'), (self.cx, self.cy), sec_end, 3)  

        
        pygame.draw.circle(surface, (20, 20, 20), (self.cx, self.cy), 10)
        pygame.draw.circle(surface, (220, 40, 40), (self.cx, self.cy), 5)