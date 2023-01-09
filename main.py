import pygame as pg
from src.screen import Screen
from src.snake import Snake
from src.timer import Timer
from src.food import Food


screen = Screen()
snake = Snake(screen)
food = Food(screen)
timer = Timer()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        snake.handle_keypress(event)

    screen.draw()

    if snake.has_colided():
        food.reset()
        snake.reset()

    food.draw()
    snake.draw()

    if timer.ready_to_render():
        snake.move()

        if snake.head.colliderect(food.point):
            snake.eat()
            food.reset()

    pg.display.flip()
    timer.tick()
