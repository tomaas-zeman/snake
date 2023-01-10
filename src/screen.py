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
        for coord in range(0, Constant.WINDOW_SIZE, Constant.TILE_SIZE):
            self.surface.blit(self.wall_sprite, pg.Rect(coord, 0, Constant.TILE_SIZE, Constant.TILE_SIZE)),
            self.surface.blit(self.wall_sprite, pg.Rect(0, coord, Constant.TILE_SIZE, Constant.TILE_SIZE)),
            self.surface.blit(
                self.wall_sprite,
                pg.Rect(coord, Constant.WINDOW_SIZE - Constant.TILE_SIZE, Constant.TILE_SIZE, Constant.TILE_SIZE),
            ),
            self.surface.blit(
                self.wall_sprite,
                pg.Rect(Constant.WINDOW_SIZE - Constant.TILE_SIZE, coord, Constant.TILE_SIZE, Constant.TILE_SIZE),
            )
