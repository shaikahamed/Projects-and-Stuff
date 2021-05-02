from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, y_cor)

    # move the paddle up and down using listeners
    def go_up(self):
        y_cor = self.ycor()
        if y_cor < 230:
            self.goto(self.xcor(), y_cor + 20)

    def go_down(self):
        y_cor = self.ycor()
        if y_cor > -230:
            self.goto(self.xcor(), y_cor - 20)
