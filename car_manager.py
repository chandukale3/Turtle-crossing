from turtle import Turtle
import random
color_list = ['blue', 'red', 'green', 'yellow', 'black', 'orange', 'purple']
starting_move_distance = 5
move_increment = 10
class Carmanager():
    def __init__(self):
        self.my_cars_list = []

    def create_new_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle('square')
            new_car.color(random.choice(color_list))
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(350,random_y)
            new_car.forward(10)
            self.my_cars_list.append(new_car)

    def move(self):
        for i in self.my_cars_list:
            i.backward(starting_move_distance)

    def increase_speed(self):
        global starting_move_distance
        starting_move_distance += move_increment