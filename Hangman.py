import turtle, random

t = turtle.Turtle()
head = turtle.Turtle()
body = turtle.Turtle()
pen = turtle.Turtle()
screen = turtle.Screen()

screen.tracer(0)

# Setting up screen
screen.setup(720, 600)
screen.title("Hangman")

# Setting up pen
t.hideturtle()
t.pensize(6)

# Setting up head
head.hideturtle()
head.penup()
head.shape("circle")
head.shapesize(2.4)
head.goto(40, 200)

# Setting up body
body.hideturtle()
body.penup()
body.pensize(6)
body.goto(40, 180)

# Setting up pen
pen.hideturtle()
pen.penup()
pen.goto(0, -150)
pen.pendown()

# Function setting up hangman
def setup():
    t.penup()
    t.goto(-120, 0)
    t.pendown()
    t.setheading(0)
    t.forward(80)
    t.penup()
    t.goto(-80, 0)
    t.setheading(90)
    t.pendown()
    t.forward(240)
    t.setheading(0)
    t.forward(120)
    t.setheading(270)
    t.forward(35)

# Fce function
def face():
    head.showturtle()

# Neck function
def neck():
    body.pendown()
    body.setheading(270)
    body.forward(25)
    body.penup()

# Arm 1 function
def arm1():
    body.setheading(225)
    body.pendown()
    body.forward(50)
    body.penup()
    body.goto(40, 155)

# Arm 2 function
def arm2():
    body.setheading(315)
    body.pendown()
    body.forward(50)
    body.penup()
    body.goto(40, 155)

# Back ffunction (chest and abs)
def back():
    body.setheading(270)
    body.pendown()
    body.forward(75)
    body.penup()

# Leg 1 function
def leg1():
    body.setheading(225)
    body.pendown()
    body.forward(60)
    body.penup()
    body.goto(40, 80)

# Leg 2 function
def leg2():
    body.setheading(315)
    body.pendown()
    body.forward(60)
    body.penup()
    body.goto(40, 80)

setup()

# Array storing man's parts 
parts = [face, neck, arm1, arm2, back, leg1, leg2]
index = -1 # Current index

screen.update()

# Letter list
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Word list
words = ["capture", "fortune", "lantern", "mission", "plastic", "gravity", "holiday", "journey", "process", "citizen"]

# Picking random word
word = random.choice(words)

# Array that will store letters or underscores
expression = []

# Filling expression with underscore for length of random word
expression = ["_ "] * len(word)

# Storing number of letters correct
length = 0

# Storing characters guessed
taken = []

# Function that takes in user guess
def guess(key):
    global letter
    letter = key

# Function that handles user guess
def find():
    global expression, letter, word, index, parts, length

    if letter not in taken:
        # Boolean that stores if guess was correct or not
        correct = False

        # Revealed characters
        revealed = 0

        for i in range(0, len(word)):
            # Letter is correct
            if letter.lower() == word[i]:
                expression[i] = letter.lower() + " "
                correct = True
                revealed += 1

        # Letter is correct
        if correct:
            length += revealed

        # Letter is incorrect
        else:
            index += 1
            parts[index]()
            screen.update()

        # Adding to taken
        taken.append(letter)

# Funciton handling key presses
def handle(n):
    # Running if game is still on
    if index < 6 and length < len(word):
        guess(n)
        find()

        # String that shows underscores and letters correct
        string = ""

        # Adding letters and underscore to string
        for i in range(len(word)):
            string += expression[i]

        # Writing string on screen
        pen.clear()
        pen.write(string, align="center", font=("Arial", 40, "bold"))

    # Outputting result
    if length == len(word):
        pen.penup()
        pen.goto(0, -220)
        pen.color("green")
        pen.pendown()
        pen.write("YOU WIN!", align="center", font=("Arial", 50, "bold"))
    elif index == 6:
        pen.penup()
        pen.goto(0, -220)
        pen.color("red")
        pen.pendown()
        pen.write("YOU LOSE!", align="center", font=("Arial", 50, "bold"))

# Show initial underscores immediately
pen.write("".join(expression), align="center", font=("Arial", 40, "bold"))
screen.update()

# Playing game
for n in alphabet:
    screen.onkeypress(lambda n=n: handle(n), n)

screen.listen()

screen.mainloop()