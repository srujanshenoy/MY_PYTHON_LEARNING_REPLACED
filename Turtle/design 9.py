import turtle as t
from colorsys import hsv_to_rgb
t.bgcolor("black")
t.tracer(100)
h = 0.2
def design():
    global h
    for i in range(4):
        for i in range(4):
            color = hsv_to_rgb(h, 1, 1)
            h += 0.002
            t.fillcolor(color)
            t.begin_fill()
            t.fd(240)
            t.rt(60)
            t.fd(10)
            t.lt(22)
            t.end_fill()
for j in range(400):
    design()
    t.goto(8,8)
    t.rt(18)
t.exitonclick()
