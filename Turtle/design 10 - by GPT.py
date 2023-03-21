import turtle
from colorsys import hsv_to_rgb

turtle.bgcolor("black")
turtle.tracer(100)
turtle.pensize(4)
h = 0.2

def design():
    global h
    color = hsv_to_rgb(h, 1, 1)
    h += 0.01
    turtle.color(color)
    turtle.fd(h)
    turtle.rt(10)

for j in range(10000):
    design()

turtle.done()
