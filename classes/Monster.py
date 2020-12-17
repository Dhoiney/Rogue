from pygame import *


MONSTER_WIDTH = 32
MONSTER_HEIGHT = 32
MONSTER_COLOR = "#ffff00"

class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, maxLengthLeft,maxLengthUp):
        sprite.Sprite.__init__(self)
        self.image = Surface((MONSTER_WIDTH, MONSTER_HEIGHT))
        self.image.fill(Color(MONSTER_COLOR))
        self.rect = Rect(x, y, MONSTER_WIDTH, MONSTER_HEIGHT)
        self.startX = x
        self.startY = y
        self.maxLengthLeft = maxLengthLeft
        self.maxLengthUp= maxLengthUp
        self.xvel = left
        self.yvel = up


# Обработка поведения врагов
    def update(self, platforms):

        self.image.fill(Color(MONSTER_COLOR))
        self.image.blit(self.image, (0, 0))
       
        self.rect.y += self.yvel
        self.rect.x += self.xvel
 
        self.collide(platforms)
        
        if (abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel =-self.xvel 
        if (abs(self.startY - self.rect.y) > self.maxLengthUp):
            self.yvel = -self.yvel


# Обработка столкновений с другими объектами
    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p) and self != p:
               self.xvel = - self.xvel
               self.yvel = - self.yvel