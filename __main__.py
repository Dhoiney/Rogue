import pygame as pg
from pygame import *
import random
from classes.Platforms import Platform

#Window param
WIN_W = 800
WIN_H = 600
DISPLAY = (WIN_W,WIN_H)
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode(DISPLAY)
BG = pg.Surface((WIN_W,WIN_H))
GAME_NAME = pg.display.set_caption("Dhoiney(c)")


#Colors
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"

#Player stat
MOVE_SPEED = 6
WIDTH = 16
HEIGHT = 16
COLOR =  "#888888"


entities = pg.sprite.Group() # all objects
platforms = [] # platforms


RUN = True


class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)


    def update(self, left, right, up, down):
        if left:
            self.xvel = -MOVE_SPEED
 
        if right:
            self.xvel = MOVE_SPEED

        if up:
            self.yvel = -MOVE_SPEED

        if down:
            self.yvel = MOVE_SPEED
         
        if not(left or right or up or down):
            self.xvel = 0
            self.yvel = 0


        self.rect.x += self.xvel
        self.rect.y += self.yvel


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x,self.rect.y))


hero = Player(74,74)
entities.add(hero)


def level():
    level = []

    y = random.randint(10, 20)
    x = random.randint(20, 30)
    trash = ""
    params = [" ", "-"]
    level.append("-" + "-" * x + "-")
    for elem in range(y):
        trash += "-"
        for item in range(x):
            trash += random.choice(params)
        trash += "-"
        if elem % 2:
            level.append(trash)
        else:
            level.append("-" + " " * x + "-")
        trash = ""

    level.append("-" + "-" * x + "-")
    return level


lvl = level()
level_len_y = (len(lvl) - 1) * 64
level_len_x = (len(lvl[1]) - 1) * 64


left = False
right = False
up = False
down = False


while RUN:
    CLOCK.tick(60)
    for elem in pg.event.get():
        if elem.type == pg.QUIT:
            RUN = False
            

    SCREEN.fill(pg.Color(BLUE))


    PLATFORM_WIDTH = 64
    PLATFORM_HEIGHT = 64
    PLATFORM_COLOR = "#FFFFFF"


    x=y=0
    for row in lvl:
        for col in row: 
            if col == "-":
                pf = Platform(x,y)
                entities.add(pf)
                platforms.append(pf)

            x += 64
        y += 64
        x = 0


    keys = pg.key.get_pressed()


    if keys[pg.K_a]:
        left = True
    elif keys[pg.K_d]:
        right = True
    elif keys[pg.K_w]:
        up = True
    elif keys[pg.K_s]:
        down = True
    else:
        left = False
        right = False
        up = False
        down = False


    hero.update(left, right, up, down)
    entities.draw(SCREEN)
    pg.display.update()



if __name__ == "__main__":
    pass