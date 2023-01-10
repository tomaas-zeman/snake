import pygame as pg
from src.screen import Screen
from src.constant import Constant


class Game:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.wasted_sprite = pg.image.load(f"sprites/wasted.png")
        self.wasted = False

    def draw(self):
        if not self.wasted:
            return

        overlay = pg.Surface((Constant.WINDOW_SIZE, Constant.WINDOW_SIZE))
        overlay.set_alpha(180)
        overlay.fill("black")
        self.screen.surface.blit(overlay, (0, 0))

        w = self.wasted_sprite.get_width()
        h = self.wasted_sprite.get_height()
        self.screen.surface.blit(
            self.wasted_sprite,
            (Constant.WINDOW_SIZE // 2 - w // 2, Constant.WINDOW_SIZE // 2 - h // 2),
        )
