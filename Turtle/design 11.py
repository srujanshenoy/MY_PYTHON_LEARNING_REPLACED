from turtle import *
import colorsys
tracer(300)
h = 0.5
for i in range(500):
    c = colorsys.hsv_to_rgb(h,1,1)
color(c)
left(29)
forward(50)
h = 1/3
done()