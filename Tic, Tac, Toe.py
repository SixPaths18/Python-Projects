import turtle, random

screen = turtle.Screen()
board = turtle.Turtle()
pen = turtle.Turtle()
line = turtle.Turtle()
game = turtle.Turtle()

# Setting up screen
screen.setup(600, 600)
screen.title("Tic, Tac, Toe")
screen.bgcolor("black")

screen.tracer(0)

# Setting up board
board.speed(0)
board.color("white")
board.hideturtle()
board.pensize(10)

def setup():
    board.setheading(90)
    # Vertical line 1
    board.penup()
    board.goto(-87.5, -250)
    board.pendown()
    board.forward(500)
    # Vertical line 2
    board.penup()
    board.goto(87.5, -250)
    board.pendown()
    board.forward(500)

    board.setheading(0)
    # Horizontal line 1
    board.penup()
    board.goto(-250, 87.5)
    board.pendown()
    board.forward(500)
    # Horizontal line 2
    board.penup()
    board.goto(-250, -87.5)
    board.pendown()
    board.forward(500)

setup()

screen.update()

# Coordinates of center of each square and filled coordinates
coordinates = [
    [-500/3, 500/3, ""], [0, 500/3, ""], [500/3, 500/3, ""],
    [-500/3, 0, ""], [0, 0, ""], [500/3, 0, ""],
    [-500/3, -500/3, ""], [0, -500/3, ""], [500/3, -500/3, ""]
]


# Setting up pen
pen.hideturtle()
pen.color("white")

# Setting up line
line.hideturtle()
line.penup()
line.pensize(10)
line.pencolor("white")
line.speed(0)

# Setting up game
game.hideturtle()
game.penup()
game.pensize(12)
game.pencolor("green")
game.speed(0)

# Font size and values to match ceter for X (y coordinates) and for O (y coordinates)
size = 80
xy = 60
oy = 60

# User inputs if they want to play 1st or 2nd
turn = screen.textinput("Turn", "Do you want to play first or second?")
# Validating input
while turn.lower() != "first" and turn.lower() != "second":
    turn = screen.textinput("Turn", "Invalid! Do you want to play first or second?")

rounds = 0
output = False

# Function detecting result
def result():
    global rounds, output

    # Horizontal wins
    if coordinates[0][2] == coordinates[1][2] == coordinates[2][2] != "":
        line.goto(-250, 500/3)
        line.setheading(0)
        line.pendown()
        line.forward(500)
        line.penup()
        screen.update()
        if coordinates[1][2] == "X":
            game.write("YOU WIN!", align="center", font=("Arial", 90, "bold"))
        else:
            game.write("YOU LOSE!", align="center", font=("Arial", 80, "bold"))
        output = True
        screen.onscreenclick(None)

    elif coordinates[3][2] == coordinates[4][2] == coordinates[5][2] != "":
        line.goto(-250, 0)
        line.setheading(0)
        line.pendown()
        line.forward(500)
        line.penup()
        screen.update()
        if coordinates[4][2] == "X":
            game.write("YOU WIN!", align="center", font=("Arial", 90, "bold"))
        else:
            game.write("YOU LOSE!", align="center", font=("Arial", 80, "bold"))
        output = True
        screen.onscreenclick(None)

    elif coordinates[6][2] == coordinates[7][2] == coordinates[8][2] != "":
        line.goto(-250, -500/3)
        line.setheading(0)
        line.pendown()
        line.forward(500)
        line.penup()
        screen.update()
        if coordinates[7][2] == "X":
            game.write("YOU WIN!", align="center", font=("Arial", 90, "bold"))        
        else:
            game.write("YOU LOSE!", align="center", font=("Arial", 80, "bold"))
        output = True
        screen.onscreenclick(None)

    # Vertical wins
    elif coordinates[0][2] == coordinates[3][2] == coordinates[6][2] != "":
        line.goto(-500/3, 250)
        line.setheading(270)
        line.pendown()
        line.forward(500)
        line.penup()
        screen.update()
        if coordinates[3][2] == "X":
            game.write("YOU WIN!", align="center", font=("Arial", 90, "bold"))
        else:
            game.write("YOU LOSE!", align="center", font=("Arial", 80, "bold"))
        output = True
        screen.onscreenclick(None)

    elif coordinates[1][2] == coordinates[4][2] == coordinates[7][2] != "":
        line.goto(0, 250)
        line.setheading(270)
        line.pendown()
        line.forward(500)
        line.penup()
        screen.update()
        if coordinates[4][2] == "X":
            game.write("YOU WIN!", align="center", font=("Arial", 90, "bold"))
        else:
            game.write("YOU LOSE!", align="center", font=("Arial", 80, "bold"))
        output = True
        screen.onscreenclick(None)

    elif coordinates[2][2] == coordinates[5][2] == coordinates[8][2] != "":
        line.goto(500/3, 250)
        line.setheading(270)
        line.pendown()
        line.forward(500)
        line.penup()
        screen.update()
        if coordinates[5][2] == "X":
            game.write("YOU WIN!", align="center", font=("Arial", 90, "bold"))
        else:
            game.write("YOU LOSE!", align="center", font=("Arial", 80, "bold"))
        output = True
        screen.onscreenclick(None)

    # Diagonal wins
    elif coordinates[0][2] == coordinates[4][2] == coordinates[8][2] != "":
        line.goto(-250, 250)
        line.setheading(315)
        line.pendown()
        line.forward(707)
        line.penup()
        screen.update()
        if coordinates[4][2] == "X":
            game.write("YOU WIN!", align="center", font=("Arial", 90, "bold"))
        else:
            game.write("YOU LOSE!", align="center", font=("Arial", 80, "bold"))
        output = True
        screen.onscreenclick(None)

    elif coordinates[2][2] == coordinates[4][2] == coordinates[6][2] != "":
        line.goto(250, 250)
        line.setheading(225)
        line.pendown()
        line.forward(707)
        line.penup()
        screen.update()
        if coordinates[4][2] == "X":
            game.write("YOU WIN!", align="center", font=("Arial", 90, "bold"))
        else:
            game.write("YOU LOSE!", align="center", font=("Arial", 80, "bold"))
        output = True
        screen.onscreenclick(None)

    # Draw
    elif rounds == 9:
        game.write("DRAW!", align="center", font=("Arial", 90, "bold"))
        output = True
        screen.onscreenclick(None)

# User playing second
if turn.lower() == "second":
    # Getting random index
    index = random.randint(0,8)
    while coordinates[index][2] != "":
        index = random.randint(0,8)
    # Moving pen to grid and writing O
    pen.penup()
    pen.goto(coordinates[index][0], coordinates[index][1] - oy)
    pen.write("O", align="center", font=("Arial", size, "bold"))
    coordinates[index][2] = "O"
    rounds += 1

# Click function
def click(x, y):
    global rounds, output

    for i in range(9): # Every index in array
        dx, dy, block = coordinates[i]

        if (x - dx)**2 + (y - dy)**2 <= 87.5**2: # User clicks in grid
            if block == "": # User clicks in empty grid
                # Moving pen to grid and writing X
                pen.penup()
                pen.goto(dx, dy - xy)
                pen.write("X", align="center", font=("Arial", size, "bold"))
                rounds += 1 # Increasing rounds
                coordinates[i][2] = "X"

                # Checking result
                result()
                if output:
                    return

                # Getting random square
                index = random.randint(0,8)
                if rounds <= 8: # Only running if rounds is withing limit
                    while coordinates[index][2] != "":
                        index = random.randint(0,8)
                    
                    # Moving pen to grid and writing O
                    pen.penup()
                    pen.goto(coordinates[index][0], coordinates[index][1] - oy)
                    pen.write("O", align="center", font=("Arial", size, "bold"))
                    coordinates[index][2] = "O"
                    rounds += 1

                # Checking result
                result()

screen.onscreenclick(click)

turtle.done()