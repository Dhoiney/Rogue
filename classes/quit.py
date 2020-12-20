from pygame import *

PORTAL_WIDTH = 64
PORTAL_HEIGHT = 64
PORTAL_COLOR = "#4e9b00"


class Quit(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PORTAL_WIDTH, PORTAL_HEIGHT))
        self.image.fill(Color(PORTAL_COLOR))
        self.rect = Rect(x, y, PORTAL_WIDTH, PORTAL_HEIGHT)
        self.x = x
        self.y = y