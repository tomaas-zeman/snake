import pygame as pg
from src.constant import Constant


class Timer:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.ticks = 0
        self.step = 100

    def tick(self):
        self.clock.tick(Constant.FPS)

    def ready_to_render(self):
        ticks = pg.time.get_ticks()
        if ticks - self.ticks > self.step:
            self.ticks = ticks
            return True
        return False
