from turtle import *
import colorsys
bgcolor("black")
tracer(200)
pensize(3)
j = 0
goto(-110, 200)
for t in range(400):
    c = colorsys.hsv_to_rgb(j, 1, 1)
    fillcolor(c)
    begin_fill()
    left(119)
    circle(50, 180)
    circle(-50, 180)
    circle(20)
    backward(350-t)
    j += 0.005
    end_fill()
done()