from pygame import *
import pygame as pg
from classes.Camera import Camera
from classes.Spike import Spike
from classes.Platforms import Platform
from classes.Monster import Monster
from classes.quit import Quit
import random

#Window params
WIN_W = 800
WIN_H = 600
DISPLAY = (WIN_W,WIN_H)
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode(DISPLAY)
GAME_NAME = pg.display.set_caption("Dhoiney(c)")

#Colors
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"

#Player stats
MOVE_SPEED = 6
EXTRA_MOVE_SPEED = 10
WIDTH = 16
HEIGHT = 16
COLOR =  "#888888"

#Platform param
PLATFORM_WIDTH = 64
PLATFORM_HEIGHT = 64


def main():
    entities = pg.sprite.Group()  # all objects
    platforms = []  # platforms
    monsters = pg.sprite.Group()  # all moving objects

    class Player(sprite.Sprite):
        def __init__(self, x, y):
            sprite.Sprite.__init__(self)
            self.xvel = 0
            self.yvel = 0
            self.startX = x
            self.startY = y
            self.image = Surface((WIDTH, HEIGHT))
            self.image.fill(Color(COLOR))
            self.rect = Rect(x, y, WIDTH, HEIGHT)

        # Обработка передвижений ГГ
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

            if not (left or right or up or down):
                self.xvel = 0
                self.yvel = 0

            self.rect.y += self.yvel
            self.collide(0, self.yvel, platforms)

            self.rect.x += self.xvel
            self.collide(self.xvel, 0, platforms)

        # Обработка столкновений ГГ
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

    def camera_configure(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t = -l + WIN_W / 2, -t + WIN_H / 2
        l = min(0, l)
        l = max(-(camera.width - WIN_W), l)
        t = max(-(camera.height - WIN_H), t)
        t = min(0, t)
        return Rect(l, t, w, h)


    # Генерация уровня
    def level():
        level = []

        y = random.randint(10, 20)
        x = random.randint(20, 30)
        trash = ""
        params = [" ", " ", " ", " ", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "*", "*", "e"]
        level.append("-" + "-" * x + "-")
        for elem in range(y):
            trash += "-"
            for item in range(x):
                trash += random.choice(params)
            trash += "-"
            if elem % 2:
                level.append(trash)
            else:
                level.append("-" + " " * x + ("-"))
            trash = ""

        level.append("-" + " " * x + ("-"))
        a = random.randint(1, (x - 2))
        level.append("-" * a + "q" + "-" * (x - a + 1))
        return level


    # Узнаем длинну и высоту уровня
    lvl = level()
    level_len_y = (len(lvl)) * PLATFORM_HEIGHT
    level_len_x = (len(lvl[1])) * PLATFORM_WIDTH

    # Создаем ГГ,добавляем ко всем объектам
    hero = Player(random.randint(64, level_len_x -64), 196)
    entities.add(hero)

    # Параметры передвижения по умолчанию
    left = False
    right = False
    up = False
    down = False

    # Перебираем список lvl и создаем объекты по символам
    x = y = 0
    for row in lvl:
        for col in row:
            if col == "-":
                pf = Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = Spike(x, y)
                entities.add(bd)
                platforms.append(bd)
            if col == "e":
                mn = Monster(x, y, 2, 0, random.randint(150, 300), random.randint(5, 15))
                entities.add(mn)
                platforms.append(mn)
                monsters.add(mn)
            if col == "q":
                quit = Quit(x, y)
                pos1 = x
                pos2 = y
                entities.add(quit)
            x += 64
        y += 64
        x = 0
    y = 0


    # Создаем объект класса Camera
    camera = Camera(camera_configure, level_len_x, level_len_y)


    # Основной игровой цикл
    run = True
    while run:
        CLOCK.tick(60)
        # Выход из игры
        for elem in pg.event.get():
            if elem.type == pg.QUIT:
                run = False
        # Заливка фона
        bg = SCREEN.fill(pg.Color(BLUE))

        # Перехват нажатий клавиш
        keys = pg.key.get_pressed()

        # Бег.По умолчанию False
        fast = False

        # Обработка нажатий на клавиши
        if hero.rect.x >= pos1 and hero.rect.y >= pos2 \
                and hero.rect.x <= pos1+64 and hero.rect.y <= pos2+64:
            return main()
        if keys[pg.K_ESCAPE]:
            run = False

        elif keys[pg.K_LSHIFT]:
            fast = True
        elif keys[pg.K_a]:
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

        # Обновление объектов
        hero.update(left, right, up, down, fast, monsters)
        camera.update(hero)
        monsters.update(platforms)

        for e in entities:
            SCREEN.blit(e.image, camera.apply(e))

            # обновление экрана
        pg.display.update()


if __name__ == "__main__":
    main()


