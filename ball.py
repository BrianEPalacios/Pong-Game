from turtle import Turtle

STARTING_BALL_X_COR = 0
STARTING_BALL_Y_COR = 0
BALL_COLOR = "white"
BALL_SHAPE = "circle"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        self.goto(x=STARTING_BALL_X_COR, y=STARTING_BALL_Y_COR)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def motion(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # changes the value of y_move
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(STARTING_BALL_X_COR, STARTING_BALL_Y_COR)
        self.move_speed = 0.1
        self.bounce_x()


