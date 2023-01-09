import pygame as pg
from src.util import get_random_position
from src.constant import Constant
from src.screen import Screen


class Snake:
    def __init__(self, screen: Screen):
        self.screen = screen
        # pg.image.load()
        self.head = pg.rect.Rect(0, 0, Constant.TILE_SIZE, Constant.TILE_SIZE)
        self.head.center = get_random_position()
        self.length = 1
        self.segments = [self.head.copy()]
        self.direction = (0, 0)

    def draw(self):
        [pg.draw.rect(self.screen.surface, "white", segment) for segment in self.segments]

    def move(self):
        self.head.move_ip(self.direction)
        self.segments = (self.segments + [self.head.copy()])[-self.length :]

    def eat(self):
        self.length += 1

    def has_colided(self):
        return (
            any([self.head.colliderect(segment) for segment in self.segments[:-1]])
            or self.head.left < Constant.TILE_SIZE
            or self.head.right > Constant.WINDOW_SIZE - Constant.TILE_SIZE
            or self.head.top < Constant.TILE_SIZE
            or self.head.bottom > Constant.WINDOW_SIZE - Constant.TILE_SIZE
        )

    def reset(self):
        self.__init__(self.screen)

    def handle_keypress(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN:
            prev_direction = self.direction
            if event.key == pg.K_UP:
                self.direction = (0, -Constant.TILE_SIZE)
            if event.key == pg.K_DOWN:
                self.direction = (0, Constant.TILE_SIZE)
            if event.key == pg.K_LEFT:
                self.direction = (-Constant.TILE_SIZE, 0)
            if event.key == pg.K_RIGHT:
                self.direction = (Constant.TILE_SIZE, 0)
            if all([abs(current) - abs(previous) == 0 for current, previous in zip(self.direction, prev_direction)]):
                self.direction = prev_direction