import turtle

# Set up the turtle screen
turtle.bgcolor('black')
turtle.pencolor('white')
turtle.speed(0)
turtle.up()
turtle.bk(600)
turtle.lt(90)
turtle.down()

# Draw the outer shape
turtle.fillcolor('white')
turtle.begin_fill()
turtle.fd(200)
turtle.rt(90)
turtle.fd(120)
# ... (more turtle commands for drawing the outer shape)

# Draw the inner details
# ... (more turtle commands for drawing the inner details)

# Hide the turtle cursor
turtle.ht()
turtle.done()
