import turtle as t
from turtle import *
from time import sleep
import objects
import random

# variables
global selected_door
door_1 = objects.Door("", 1, 25, -50)
door_2 = objects.Door("", 1, 95, -50)
door_3 = objects.Door("", 1, 165, -50)

#setup
Window = Screen()
Window.title('Monty Hall')
goto(0, 0)
for i in range(0, 3):
    fillcolor("#808080")
    begin_fill()
    for j in range(0, 2):
        fd(50)
        rt(90)
        fd(100)
        rt(90)
    penup()
    fd(70)
    pendown()
    end_fill()

hideturtle()
# goto(25, -50)
# write('🚉')


#door selection
selected_door = random.randint(1, 3)
if selected_door == 1:
    door_1.prize = "🚆"
    door_2.prize = "🐐"
    door_3.prize = "🐐"

elif selected_door == 2:
    door_2.prize = "🚆"
    door_1.prize = "🐐"
    door_3.prize = "🐐"
elif selected_door == 3:
    door_3.prize == "🚆"
    door_2.prize == "🐐"
    door_1.prize == "🐐"

print(selected_door)
door_1.reveal()
door_2.reveal()
door_3.reveal()


sleep(1)


