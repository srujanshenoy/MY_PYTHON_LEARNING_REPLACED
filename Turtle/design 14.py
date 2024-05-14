import turtle as t
import colorsys as cs

t.setup(300,300)
t.speed(-100000000000)
t.tracer(1000)
t.width(30)
t.bgcolor("black")

for j in range(26):
    for i in range(15):
        t.color(cs.hsv_to_rgb(i/15, j/25, 1))
        t.right(90)
        t.circle(150-j*4, 90)
        t.left(90)
        t.circle(150 - j * 4, 90)
        t.right(180)
        t.circle(50, 24)

t.exitonclick()

