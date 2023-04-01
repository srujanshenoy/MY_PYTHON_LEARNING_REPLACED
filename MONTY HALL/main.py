# import turtle as t
# from turtle import *
# from time import sleep
# import objects
# import random
#
# # variables
# global selected_door
# door_1 = objects.Door("", 1, 25, -50)
# door_2 = objects.Door("", 1, 95, -50)
# door_3 = objects.Door("", 1, 165, -50)
#
# #setup
# Window = Screen()
# Window.title('Monty Hall')
# goto(0, 0)
# for i in range(0, 3):
#     fillcolor("#808080")
#     begin_fill()
#     for j in range(0, 2):
#         fd(50)
#         rt(90)
#         fd(100)
#         rt(90)
#     penup()
#     fd(70)
#     pendown()
#     end_fill()
#
# hideturtle()
# # goto(25, -50)
# # write('🚉')
#
#
# #door selection
# selected_door = random.randint(1, 3)
# if selected_door == 1:
#     door_1.prize = "🚆"
#     door_2.prize = "🐐"
#     door_3.prize = "🐐"
#
# elif selected_door == 2:
#     door_2.prize = "🚆"
#     door_1.prize = "🐐"
#     door_3.prize = "🐐"
# elif selected_door == 3:
#     door_3.prize == "🚆"
#     door_2.prize == "🐐"
#     door_1.prize == "🐐"
#
# print(selected_door)
# door_1.reveal()
# door_2.reveal()
# door_3.reveal()
#
#
# sleep(1)
#
#


import pygame
import random

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Monty Hall Game")

# Set up the doors
door_width = 150
door_height = 300
door_margin = 50
doors = []
for i in range(3):
    door_x = door_margin + (door_width + door_margin) * i
    door_y = screen_height / 2 - door_height / 2
    doors.append(pygame.Rect(door_x, door_y, door_width, door_height))

# Set up the buttons
button_width = 100
button_height = 50
button_margin = 10
buttons = []
for i in range(2):
    button_x = screen_width / 2 - (button_width + button_margin) * 2 + (button_width + button_margin) * i
    button_y = screen_height - button_height - 20
    buttons.append(pygame.Rect(button_x, button_y, button_width, button_height))

# Set up the game state
winning_door = random.randint(0, 2)
selected_door = None
revealed_door = None

# Set up the fonts
font = pygame.font.SysFont(None, 30)

# Set up the sound effects
# win_sound = pygame.mixer.Sound("win.wav")
# lose_sound = pygame.mixer.Sound("lose.wav")

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for i, door in enumerate(doors):
                if door.collidepoint(pos) and selected_door is None and i != winning_door:
                    revealed_door = i
                    break
            for i, button in enumerate(buttons):
                if button.collidepoint(pos) and i == 0:
                    selected_door = revealed_door
                    break
                elif button.collidepoint(pos) and i == 1:
                    # if selected_door == winning_door:
                        # win_sound.play()
                    # else:
                        # lose_sound.play()
                    running = False

    # Update the screen
    screen.fill((255, 255, 255))
    for i, door in enumerate(doors):
        if i == selected_door:
            pygame.draw.rect(screen, (0, 0, 255), door)
        elif i == revealed_door:
            pygame.draw.rect(screen, (255, 0, 0), door)
        else:
            pygame.draw.rect(screen, (128, 128, 128), door)
    for i, button in enumerate(buttons):
        if i == 0:
            pygame.draw.rect(screen, (0, 255, 0), button)
            text = font.render("Stay", True, (255, 255, 255))
            text_rect = text.get_rect(center=button.center)
            screen.blit(text, text_rect)
        elif i == 1:
            pygame.draw.rect(screen, (255, 0, 0), button)
            text = font.render("Switch", True, (255, 255, 255))
            text_rect = text.get_rect(center=button.center)
            screen.blit(text, text_rect)
    pygame.display.flip()

pygame.quit()
