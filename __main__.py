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
backgroud = pg.image.load("res/menu.jpg")

# Text
text = pg.font.SysFont('arial', 36)
pg.font.Font('res/Arial.ttf', 36)
text_new_game = text.render('Новая Игра',True, (255, 255, 255))
text_continue = text.render('Продолжить',True, (255, 255, 255))
text_exit = text.render('Выход',True, (255, 255, 255))


RUN = True
pos_menu = 190
while RUN:
    CLOCK.tick(60)

    SCREEN.blit(backgroud, (0, 0))
    pg.draw.rect(SCREEN, (84, 255, 159), (300, pos_menu, 250, 60), 4)
    SCREEN.blit(text_new_game, (320, 200))
    SCREEN.blit(text_continue, (320, 300))
    SCREEN.blit(text_exit, (320, 400))
    keys = pg.key.get_pressed()
    for elem in pg.event.get():

        # Событие для выхода из игры
        if elem.type == pg.QUIT:
            RUN = False

        # Клавиши управления
        elif keys[pg.K_s]:
            pos_menu += 100
            if pos_menu > 400:
                pos_menu = 190
        elif keys[pg.K_w]:
            pos_menu -= 100
            if pos_menu < 190:
                pos_menu = 390

        if keys[pg.K_SPACE]:
            if pos_menu == 190:
                game.main()
            elif pos_menu == 390:
                RUN = False


    pg.display.update()


