import turtle

screen = turtle.Screen()
line = turtle.Turtle()
circle = turtle.Turtle()
pen = turtle.Turtle()
writer = turtle.Turtle()

# Setting up screen title, dimensions and colour
screen.title("Calculator")
screen.setup(450, 610)
screen.bgcolor("black")

screen.tracer(0)

# Setting up circle drawer
circle.speed(0)
circle.penup()
circle.color("grey")
circle.shapesize(4)
circle.shape("circle")

# Initial x and y coordinates 
x = -147
y = 102.5

for i in range(4): # Looping 4 times (y coordinate)
    for j in range(4): # Looping 4 times (x coordinates)
        circle.goto(x, y)
        circle.stamp()

        # Updating x coordinate
        x += 98
    
    # Updating x and y coordinates
    x = -147
    y -= 115

circle.hideturtle()

# Drawing line for calculator screen
line.speed(0)
line.color("grey")
line.penup()
line.pensize(3)
line.goto(-200, 180)
line.pendown()
line.forward(400)
line.left(90)
line.forward(100)
line.left(90)
line.forward(400)
line.left(90)
line.forward(100)
line.hideturtle()

# Storing buttons in array
buttons = [
    "7", "8", "9", "C",
    "4", "5", "6", "/",
    "1", "2", "3", "*",
    "0", "=", "+", "-"
]

# Array of coordinates for buttons
button_coordinates = []

# Initital index is 0 
index = 0

# Setting up pen to write numbers and symbols
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.pencolor("white")

# Initial x and y coordinates 
x = -147
y = 81

for i in range(4): # Looping 4 times (y coordinates)
    for j in range(4): # Looping 4 times (x coordinates)
        # Writing buttons
        pen.goto(x, y)
        pen.write(buttons[index], align="center", font=("Arial", 30, "bold"))

        # Adding coordinates of each button to array
        button_coordinates.append([x, (y+21.5), buttons[index]])

        # Incrementing index
        index += 1

        # Updating x coordinates 
        x += 98

    # Updating x and y coordinates
    x = -147
    y -= 115

screen.update()

# Creating expression for calculation
expression = ""

# Setting up writer to write calculation
writer.color("white")
writer.goto(0, 200)

# Function to write users calculation
def click(x, y):
    global expression

    # Loop going through all buttons
    for dx, dy, button in button_coordinates:
        # Performing user's click if click was on button
        if (x - dx)**2 + (y - dy)**2 <= 40**2:
            # Clearing
            if button == "C":
                expression = ""
                writer.clear()

            # Giving answer
            elif button == "=":
                # Valid answer
                try: 
                    expression = eval(expression)
                    writer.clear()
                    writer.write(expression, align="center", font=("Arial", 30, "bold"))
                    expression = ""
                # Divison by zero and math error
                except ZeroDivisionError:
                    writer.clear()
                    expression = "Math Error"
                    writer.write(expression, align="center", font=("Arial", 30, "italic"))
                    expression = ""
                
                # Invalid expression and syntax error
                except:
                    writer.clear()
                    expression = "Syntax Error"
                    writer.write(expression, align="center", font=("Arial", 30, "italic"))
                    expression = ""

            # Writing expression
            else:
                expression += str(button)
                writer.clear()
                writer.write(expression, align="center", font=("Arial", 30, "bold"))

screen.onscreenclick(click)

screen.mainloop()