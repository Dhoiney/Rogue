from pygame import *
import pygame as pg
import game

pg.font.init()

# Window params
WIN_W = 800
WIN_H = 600
DISPLAY = (WIN_W, WIN_H)
CLOCK = pg.time.Clock()
SCREEN = pg.display.set_mode(DISPLAY)
GAME_NAME = pg.display.set_caption("Dhoiney(c)")

# Background Image
backgroud = pg.image.load("menu.jpg")

# Text
text = pg.font.SysFont('arial', 36)
pg.font.Font('res/Arial.ttf', 36)
text_new_game = text.render('Новая Игра',True, (255, 255, 255))
text_continue = text.render('Продолжить',True, (255, 255, 255))
text_exit = text.render('Выход',True, (255, 255, 255))


RUN = True
pos_menu = 200
while RUN:
    CLOCK.tick(60)
    # Выход из игры
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(backgroud, (0, 0))
    pg.draw.rect(SCREEN, (64, 128, 255), (300, pos_menu, 250, 60), 8)
    SCREEN.blit(text_new_game, (320, 200))
    SCREEN.blit(text_continue, (320, 300))
    SCREEN.blit(text_exit, (320, 400))
    keys = pg.key.get_pressed()
    for elem in pg.event.get():

        if elem.type == pg.QUIT:
            RUN = False

        elif keys[pg.K_s]:
            pos_menu += 100
            if pos_menu > 400:
                pos_menu = 200
        elif keys[pg.K_w]:
            pos_menu -= 100
            if pos_menu < 200:
                pos_menu = 400

        if keys[pg.K_SPACE]:
            if pos_menu == 200:
                game.main()
            elif pos_menu == 400:
                RUN = False


    pg.display.update()


