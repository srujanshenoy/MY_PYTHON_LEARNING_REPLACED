from turtle import *
color("#f73487")
bgcolor("black")
speed(0)
right(45)
for i in range(150):
    circle(30)
    if 7 < i < 62:
        left(5)
    if 80 < i < 133:
        right(5)
        circle(30)
    if i < 80:
        forward(10)
    else:
        forward(5)
exitonclick()
