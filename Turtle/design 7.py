import turtle as t
import colorsys
t.bgcolor("black")
t.pensize(100)
t.tracer(1)
t.speed(0)
h = 0
for i in range(300):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.005
    t.color(c)
    t.left(100)
    t.up()
    t.forward(i)
    t.down()
    t.circle(i, -90)
    t.right(200)
    t.up()
    t.forward(i)
    t.left(120)
    t.forward(i)
    t.down()

t.exitonclick()
