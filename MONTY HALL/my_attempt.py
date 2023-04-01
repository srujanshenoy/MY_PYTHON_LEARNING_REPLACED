import pygame as py
import time as ti

screen_height = 900
screen_width = 900
window = py.display.set_mode((screen_height, screen_width))
doors = []
#setup doors
door_height = 100
door_width = 50
door_margin = 10
for i in range (0, 2):
    doors.append(py.Rect())
ti.sleep(1)