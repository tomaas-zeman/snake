import pygame as pg
from src.constant import Constant


class Screen:
    def __init__(self):
        pg.display.set_caption("Snek 2D")
        self.surface = pg.display.set_mode([Constant.WINDOW_SIZE, Constant.WINDOW_SIZE])

    def draw(self):
        self.surface.fill("black")
        [
            pg.draw.rect(self.surface, "grey", wall)
            for wall in [
                pg.rect.Rect(0, 0, Constant.WINDOW_SIZE, Constant.TILE_SIZE),
                pg.rect.Rect(0, Constant.WINDOW_SIZE - Constant.TILE_SIZE, Constant.WINDOW_SIZE, Constant.TILE_SIZE),
                pg.rect.Rect(0, 0, Constant.TILE_SIZE, Constant.WINDOW_SIZE),
                pg.rect.Rect(Constant.WINDOW_SIZE - Constant.TILE_SIZE, 0, Constant.TILE_SIZE, Constant.WINDOW_SIZE),
            ]
        ]
