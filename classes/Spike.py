from pygame import *
from classes.Platforms import Platform

COLOR = "#FF0000"


class Spike(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load('res/spike.xcf')