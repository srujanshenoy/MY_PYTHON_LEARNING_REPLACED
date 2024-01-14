import turtle as t
import time as ti

current_time = 10  # set this to the value in seconds


def display_time(time):
    t.penup()
    t.clear()
    t.write(time, font=("Arial", 50, "normal"))


def timer(seconds):
    while seconds:
        minutes, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, secs)
        display_time(time_format)
        ti.sleep(1)
        seconds -= 1

    t.clear()
    t.write("Time's up!", font=("Arial", 50, "normal"))
    ti.sleep(5)


timer(current_time)
