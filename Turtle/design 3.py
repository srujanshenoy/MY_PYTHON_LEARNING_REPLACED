# Thanks, programmingpuzzles8862@youtube

from turtle import*
from colorsys import*
bgcolor ('black')
tracer(5)
h = 0.4
for i in range (250):
    c = hsv_to_rgb(h,1, 1)
    color(c)
    h += 0.005
    width(i//100+3)
    fillcolor(c)
    left(59)
    begin_fill()
    forward(i * 0.5)
    circle(i * 0.3)
    end_fill()
    right (90)
    circle(i,90)
    circle(i, 60)
done()