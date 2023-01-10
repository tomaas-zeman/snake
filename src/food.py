import pygame as pg
from src.util import get_random_position
from src.constant import Constant
from src.screen import Screen


class Food:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.sprite = pg.transform.scale(pg.image.load(f"sprites/food.png"), (Constant.TILE_SIZE, Constant.TILE_SIZE))
        self.location = pg.Rect(0, 0, Constant.TILE_SIZE, Constant.TILE_SIZE)
        self.location.center = get_random_position()

    def draw(self):
        self.screen.surface.blit(self.sprite, self.location)

    def reset(self):
        self.__init__(self.screen)
