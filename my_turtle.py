from turtle import Turtle, Screen
my_screen = Screen()
class Myturtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
    def move_forward(self):
        self.forward(10)
    def move(self):
        my_screen.listen()
        my_screen.onkey(key='Up', fun= self.move_forward)
    def reset_position(self):
        self.goto(0, -280)