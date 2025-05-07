from turtle import Turtle, Screen
from car_manager import Carmanager
from my_turtle import Myturtle
from scoreboard import Scoreboard
import time as t
my_screen = Screen()
my_screen.screensize(800,600)
my_screen.title('Turtle Crossing game')
my_screen.bgcolor('white')
my_screen.tracer(0)
car_manager = Carmanager()
game_turtle = Myturtle()
my_scoreboard = Scoreboard()
game_over = False
while not game_over:
    t.sleep(0.1)
    car_manager.create_new_car()
    car_manager.move()
    game_turtle.move()
    my_scoreboard.level_up()
    if game_turtle.ycor() > 300:
        my_scoreboard.level += 1
        game_turtle.reset_position()
        car_manager.increase_speed()
    for j in car_manager.my_cars_list:
        if game_turtle.distance(j) < 26:
            my_scoreboard.game_over()
            game_over = True
    my_screen.update()













my_screen.exitonclick()