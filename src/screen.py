import pygame as pg
from src.constant import Constant


class Screen:
    def __init__(self):
        pg.display.set_caption("Snek 2D")
        self.surface = pg.display.set_mode([Constant.WINDOW_SIZE, Constant.WINDOW_SIZE])
        self.wall_sprite = pg.transform.scale(
            pg.image.load(f"sprites/wall.png"), (Constant.TILE_SIZE, Constant.TILE_SIZE)
        )

    def draw(self):
        self.surface.fill("black")
        [
            self.surface.blit(self.wall_sprite, pg.rect.Rect(x, 0, Constant.TILE_SIZE, Constant.TILE_SIZE))
            for x in range(0, Constant.WINDOW_SIZE, Constant.TILE_SIZE)
        ]
        [
            self.surface.blit(
                self.wall_sprite,
                pg.rect.Rect(x, Constant.WINDOW_SIZE - Constant.TILE_SIZE, Constant.TILE_SIZE, Constant.TILE_SIZE),
            )
            for x in range(0, Constant.WINDOW_SIZE, Constant.TILE_SIZE)
        ]
        [
            self.surface.blit(self.wall_sprite, pg.rect.Rect(0, y, Constant.TILE_SIZE, Constant.TILE_SIZE))
            for y in range(0, Constant.WINDOW_SIZE, Constant.TILE_SIZE)
        ]
        [
            self.surface.blit(
                self.wall_sprite,
                pg.rect.Rect(Constant.WINDOW_SIZE - Constant.TILE_SIZE, y, Constant.TILE_SIZE, Constant.TILE_SIZE),
            )
            for y in range(0, Constant.WINDOW_SIZE, Constant.TILE_SIZE)
        ]
