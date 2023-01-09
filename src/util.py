from random import randrange
from src.constant import Constant


def get_random_position():
    range = (
        Constant.TILE_SIZE + Constant.TILE_SIZE // 2,
        Constant.WINDOW_SIZE - Constant.TILE_SIZE * 1.5,
        Constant.TILE_SIZE,
    )
    return randrange(*range), randrange(*range)
