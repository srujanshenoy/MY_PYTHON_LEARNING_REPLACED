import turtle
import math

t = turtle.Turtle()
t.speed(0)

a = 0.1 # coefficient
b = 0.2 # exponent

for theta in range(0, 720):
    r = a * math.exp(b * theta / 360 * 2 * math.pi) # polar equation of logarithmic spiral
    x = r * math.cos(theta / 360 * 2 * math.pi) # convert to cartesian coordinates
    y = r * math.sin(theta / 360 * 2 * math.pi)
    t.goto(x, y)

turtle.done()