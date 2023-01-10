import pygame as pg
from src.screen import Screen
from src.snake import Snake
from src.timer import Timer
from src.food import Food
from src.game import Game


screen = Screen()
snake = Snake(screen)
food = Food(screen)
timer = Timer()
game = Game(screen)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if game.wasted:
            if event.type == pg.KEYDOWN and event.key in [pg.K_SPACE, pg.K_RETURN, pg.K_ESCAPE]:
                food.reset()
                snake.reset()
                game.wasted = False
        else:
            snake.handle_keypress(event)

    screen.draw()
    food.draw()
    snake.draw()
    game.draw()

    if snake.wasted:
        game.wasted = True
    elif timer.ready_to_render():
        snake.move()
        if snake.head_location.colliderect(food.location):
            snake.eat()
            food.reset()

    pg.display.flip()
    timer.tick()
