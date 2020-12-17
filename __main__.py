import pygame as pg
from pygame import *
import random
from classes.Platforms import Platform
from classes.Camera import Camera
from classes.Spike import Spike
from classes.Monster import Monster

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
EXTRA_MOVE_SPEED = 10
WIDTH = 16
HEIGHT = 16
COLOR =  "#888888"


#Platform param
PLATFORM_WIDTH = 64
PLATFORM_HEIGHT = 64


entities = pg.sprite.Group() # all objects
platforms = [] # platforms
monsters = pg.sprite.Group()  # all moving objects


RUN = True


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_W / 2, -t + WIN_H / 2
    l = min(0, l)
    l = max(-(camera.width-WIN_W), l)
    t = max(-(camera.height-WIN_H), t)
    t = min(0, t)
    return Rect(l, t, w, h)


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


    def update(self, left, right, up, down, fast, monsters):
        if left:
            self.xvel = -MOVE_SPEED
            if fast:
                self.xvel -= EXTRA_MOVE_SPEED
 
        if right:
            self.xvel = MOVE_SPEED
            if fast:
                self.xvel += EXTRA_MOVE_SPEED

        if up:
            self.yvel = -MOVE_SPEED
            if fast:
                self.yvel -= EXTRA_MOVE_SPEED

        if down:
            self.yvel = MOVE_SPEED
            if fast:
                self.yvel += EXTRA_MOVE_SPEED

         
        if not(left or right or up or down):
            self.xvel = 0
            self.yvel = 0


        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
    
        self.rect.x += self.xvel 
        self.collide(self.xvel, 0, platforms)


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top

                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0


                if isinstance(p, Spike) or isinstance(p, Monster):
                    self.die()

    
    def die(self):
        time.wait(500)
        self.teleporting(self.startX, self.startY)

    
    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY


hero = Player(74,74)
entities.add(hero)


def level():
    level = []

    y = random.randint(10, 20)
    x = random.randint(20, 30)
    trash = ""
    params = [" ", " "," ", " ", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "*", "e"]
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
level_len_y = (len(lvl) - 1) * PLATFORM_HEIGHT
level_len_x = (len(lvl[1]) - 1) * PLATFORM_WIDTH


left = False
right = False
up = False
down = False

   
camera = Camera(camera_configure, level_len_x, level_len_y) 


while RUN:
    CLOCK.tick(60)
    for elem in pg.event.get():
        if elem.type == pg.QUIT:
            RUN = False


    SCREEN.fill(pg.Color(BLUE))


    x=y=0
    for row in lvl:
        for col in row: 
            if col == "-":
                pf = Platform(x,y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = Spike(x,y)
                entities.add(bd)
                platforms.append(bd)
            if col == "e":
                mn = Monster(x,y,2,3,random.randint(150,300),random.randint(5,15))
                entities.add(mn)
                platforms.append(mn)
                monsters.add(mn)
            x += 64
        y += 64
        x = 0
        

    keys = pg.key.get_pressed()
    fast = False


    if keys[pg.K_ESCAPE]:
        RUN = False


    if keys[pg.K_LSHIFT]:
        fast = True
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


    hero.update(left, right, up, down, fast, monsters)
    camera.update(hero)
    monsters.update(platforms)
    

    for e in entities:
        SCREEN.blit(e.image, camera.apply(e))


    pg.display.update()