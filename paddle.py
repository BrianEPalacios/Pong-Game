from turtle import Turtle

COLOR = "white"
SHAPE = "square"
Y_PADDLE_POSITION = 0
MOVE_PADDLE_UP_DOWN = 20


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        x_cor = x_position
        self.penup()
        self.color(COLOR)
        self.shape(SHAPE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=x_cor, y=Y_PADDLE_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_PADDLE_UP_DOWN
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_PADDLE_UP_DOWN
        self.goto(self.xcor(), new_y)