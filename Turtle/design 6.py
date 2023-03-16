from turtle import *
import colorsys
bgcolor("black")
tracer(400)
pensize(3)
h = 0
for i in range(400):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    pencolor(c)
    begin_fill()
    circle(-20, 240)
    right(59)
    forward(i * 0.5)
    circle(20, 120)
    left(120)
    backward(i * 0.5)
    h += 0.005
    end_fill()
exitonclick()