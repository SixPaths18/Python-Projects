import turtle

screen = turtle.Screen()
t = turtle.Turtle()

# Setting up screen
screen.setup(720, 600)
screen.title("Golden Fibonacci spiral")
screen.bgcolor("black")

# Setting up turtle
t.hideturtle()
t.speed(0)
t.pensize(3.6)
t.setheading(270)
t.pencolor("white")
t.penup()
t.goto(100, 0)
t.pendown()

# Fibonacci sequence
fibonacci = [1, 1, 2, 3, 5, 8, 13, 21]

# Scale, index and angle of drawing
scale = 4
index = 0
angle = 1

# Drawing till length of fibonacci
for i in range(len(fibonacci)):
    # Drawing quarter circle
    for i in range(90):
        # Moving forward and turning
        t.forward(fibonacci[index]/scale)
        t.left(angle)

    # Incrementing index
    index += 1

screen.mainloop()