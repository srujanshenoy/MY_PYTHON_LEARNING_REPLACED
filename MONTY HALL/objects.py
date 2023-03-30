from turtle import *
class Door:
    def __init__(self, prize, state, xcor, ycor):
        self.prize = prize
        self.state = state
        self.xcor = xcor
        self.ycor = ycor

    def reveal(self):
        pendown()
        if self.state == 'open' or self.state == 1:
            penup()
            goto(self.xcor, self.ycor)
            write(self.prize)
        elif self.state == 'close' or self.state == 0:
            pass
        else:
            raise
        penup()