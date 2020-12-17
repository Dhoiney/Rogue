from pygame import *


PLATFORM_WIDTH = 64
PLATFORM_HEIGHT = 64


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load("res/wall_tile.xcf")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)