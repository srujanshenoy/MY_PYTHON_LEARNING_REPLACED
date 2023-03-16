from turtle import *
def func():
    i = 0
    fillcolor("red")
    begin_fill()
    while i < 2:
        fd(100)
        rt(90)
        fd(50)
        rt(90)
        i += 1
    end_fill()
    penup()
    goto(50, 25)
    pendown()
    i = 0
    fillcolor("white")
    begin_fill()
    while i < 3:
        fd(25)
        rt(60)
        i += 1
    end_fill()

func()
exitonclick()