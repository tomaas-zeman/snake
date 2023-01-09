import pygame as pg
from src.util import get_random_position
from src.constant import Constant
from src.screen import Screen


class Food:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.point = pg.rect.Rect(0, 0, Constant.TILE_SIZE, Constant.TILE_SIZE)
        self.point.center = get_random_position()

    def draw(self):
        pg.draw.rect(self.screen.surface, "green", self.point)

    def reset(self):
        self.__init__(self.screen)
