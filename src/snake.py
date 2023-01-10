import pygame as pg
from src.util import get_random_position
from src.constant import Constant
from src.screen import Screen


class Snake:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.head_location = pg.rect.Rect(0, 0, Constant.TILE_SIZE, Constant.TILE_SIZE)
        self.head_location.center = get_random_position()
        self.length = 1
        self.direction = (0, 0)
        self.segments = [self.head_location.copy()]

        self.sprites = {
            sprite: pg.transform.scale(pg.image.load(f"sprites/{sprite}.png"), (Constant.TILE_SIZE, Constant.TILE_SIZE))
            for sprite in ["head", "tail", "body", "curve"]
        }
        self.rendered_sprites = {sprite: self.sprites[sprite].copy() for sprite in ["head", "tail", "body", "curve"]}

    def draw(self):
        def blit(sprite: str, segment: pg.rect.Rect, angle: int = 0):
            self.screen.surface.blit(pg.transform.rotate(self.sprites[sprite], angle), segment)

        for i, segment in enumerate(self.segments[::-1]):
            if i == 0:
                angle = 0
                if self.direction[0] > 0:  # right
                    angle = 180
                elif self.direction[0] < 0:  # left
                    angle = 0
                elif self.direction[1] > 0:  # down
                    angle = 90
                elif self.direction[1] < 0:  # up
                    angle = -90
                blit("head", segment, angle)
            elif i == len(self.segments) - 1:
                angle = 0
                prev_segment = self.segments[::-1][i - 1]
                if prev_segment.centerx < segment.centerx:
                    angle = 0
                elif prev_segment.centerx > segment.centerx:
                    angle = 180
                elif prev_segment.centery < segment.centery:
                    angle = -90
                elif prev_segment.centery > segment.centery:
                    angle = 90
                blit("tail", segment, angle)
            else:
                angle = 0
                prev_segment = self.segments[::-1][i - 1]
                next_segment = self.segments[::-1][i + 1]

                sprite = "body"
                if prev_segment.centerx != next_segment.centerx and prev_segment.centery != next_segment.centery:
                    sprite = "curve"
                    if prev_segment.centerx < next_segment.centerx:
                        if prev_segment.centery < next_segment.centery:
                            if segment.centerx == prev_segment.centerx:
                                angle = 180
                            else:
                                angle = 0
                        else:
                            if segment.centerx == prev_segment.centerx:
                                angle = 90
                            else:
                                angle = -90
                    elif prev_segment.centerx > next_segment.centerx:
                        if prev_segment.centery < next_segment.centery:
                            if segment.centerx == prev_segment.centerx:
                                angle = -90
                            else:
                                angle = 90
                        else:
                            if segment.centerx == prev_segment.centerx:
                                angle = 0
                            else:
                                angle = 180
                else:
                    if prev_segment.centerx < segment.centerx:
                        angle = -90
                    elif prev_segment.centerx > segment.centerx:
                        angle = 90
                    elif prev_segment.centery < segment.centery:
                        angle = 0
                    elif prev_segment.centery > segment.centery:
                        angle = 180
                blit(sprite, segment, angle)

    def move(self):
        self.head_location.move_ip(self.direction)
        self.segments = (self.segments + [self.head_location.copy()])[-self.length :]

    def eat(self):
        self.length += 1

    def has_colided(self):
        return (
            any([self.head_location.colliderect(segment) for segment in self.segments[:-1]])
            or self.head_location.left < Constant.TILE_SIZE
            or self.head_location.right > Constant.WINDOW_SIZE - Constant.TILE_SIZE
            or self.head_location.top < Constant.TILE_SIZE
            or self.head_location.bottom > Constant.WINDOW_SIZE - Constant.TILE_SIZE
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
