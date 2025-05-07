from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.level = 0

    def level_up(self):
        self.goto(-290, 280)
        self.clear()
        self.write(f'Level = {self.level}', move=False, align='center', font=('Courier', 20, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER', move=False, align='center', font=('Courier', 30, 'normal'))
