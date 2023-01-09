import pygame as pg
from random import randrange

WINDOW = 800
FPS = 60

SEGMENT_SIZE = 50
RANGE = (SEGMENT_SIZE + SEGMENT_SIZE // 2, WINDOW - SEGMENT_SIZE - SEGMENT_SIZE // 2, SEGMENT_SIZE)

screen = pg.display.set_mode([WINDOW, WINDOW])
clock = pg.time.Clock()

time = 0
time_step = 100

# px of the middle of a cell
def get_random_position():
    return randrange(*RANGE), randrange(*RANGE)


snek = pg.rect.Rect(0, 0, SEGMENT_SIZE - 2, SEGMENT_SIZE - 2)
snek.center = get_random_position()
snek_length = 1
snek_segments = [snek.copy()]
snek_direction = (0, 0)  # change in coords per frame

food = pg.rect.Rect(0, 0, SEGMENT_SIZE - 2, SEGMENT_SIZE - 2)
food.center = get_random_position()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            prev_direction = snek_direction
            if event.key == pg.K_UP:
                snek_direction = (0, -SEGMENT_SIZE)
            if event.key == pg.K_DOWN:
                snek_direction = (0, SEGMENT_SIZE)
            if event.key == pg.K_LEFT:
                snek_direction = (-SEGMENT_SIZE, 0)
            if event.key == pg.K_RIGHT:
                snek_direction = (SEGMENT_SIZE, 0)
            if all([abs(snek) - abs(prev) == 0 for snek, prev in zip(snek_direction, prev_direction)]):
                snek_direction = prev_direction

    # draw screen
    screen.fill("black")
    [
        pg.draw.rect(screen, "grey", wall)
        for wall in [
            pg.rect.Rect(0, 0, WINDOW, SEGMENT_SIZE),
            pg.rect.Rect(0, WINDOW - SEGMENT_SIZE, WINDOW, SEGMENT_SIZE),
            pg.rect.Rect(0, 0, SEGMENT_SIZE, WINDOW),
            pg.rect.Rect(WINDOW - SEGMENT_SIZE, 0, SEGMENT_SIZE, WINDOW),
        ]
    ]

    # reset snek in case of a collision
    if (
        any([snek.colliderect(segment) for segment in snek_segments[:-1]])
        or snek.left < SEGMENT_SIZE
        or snek.right > WINDOW - SEGMENT_SIZE
        or snek.top < SEGMENT_SIZE
        or snek.bottom > WINDOW - SEGMENT_SIZE
    ):

        food.center = get_random_position()
        snek.center = get_random_position()
        snek_length = 1
        snek_direction = (0, 0)
        segments = [snek.copy()]

    # draw food
    pg.draw.rect(screen, "green", food)

    # draw snek
    [pg.draw.rect(screen, "white", segment) for segment in snek_segments]

    # update snek
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snek = snek.move(snek_direction)
        snek_segments.append(snek)
        snek_segments = snek_segments[-snek_length:]

        if snek.colliderect(food):
            snek_length += 1
            food.center = get_random_position()

    pg.display.flip()
    clock.tick(FPS)
