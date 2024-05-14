import turtle as t
from colorsys import hsv_to_rgb
t.bgcolor("black")
t.width(0.1)
t.tracer(10)
h = 0.2
def design():
    global h
    for i in range(5):
        for i in range(2):
            color = hsv_to_rgb(h, 1, 1)
            h += 0.002
            t.fillcolor(color)
            t.begin_fill()
            # # t.fd(240)
            # t.fd(150)
            # # t.rt(60)
            # t.rt(90)
            # # t.fd(10)
            t.circle(i, -90)
            t.fd(6.25)
            t.lt(22)
            t.end_fill()
for j in range(400):
    design()
    t.goto(8,8)
    t.rt(18)
t.exitonclick()
