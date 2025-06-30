# Importing turtle and random module
import turtle 
import random

segments = []   # Snake's body length

pen = turtle.Turtle()
t = turtle.Turtle()   # Snake
apple = turtle.Turtle()   # Apple
screen = turtle.Screen()   # Screen
x = random.randint(-310, 310)   # Apple x coordinate
y = random.randint(-300, 300)   # Apple y coordinate

# Screen title, size, gackground color(green grass)
screen.title("Snake Game")
screen.setup(650, 650)
screen.bgcolor("green")

# Snake shape, speed
t.shape("square")
t.speed(0)

# Apple shape, color, initital random position
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(x, y)

# Boundary coordinates
boundary_forward = 310
boundary_down = -300
boundary_right = 300
boundary_left = -310

# Snake starts off moving north
current_direction = 90

# Score
score = 0

# Going to top of screen and writing score
pen.penup()
pen.goto(0, 270)
pen.write("Score = 0", font=("Arial", 18), align="center")

# Snake speed high
t.speed(10000000000)

# Snake head not collide with body
game_over = False

# Move function
def move():
    global segments, segment, score, game_over
    pen.hideturtle()
    if game_over == False:
        if boundary_down < t.ycor() < boundary_forward and boundary_left < t.xcor() < boundary_right:   # Snake is within board(x and y coordinates within boundaries) 
            t.setheading(current_direction)   # Snake heading in current direction (updated in forward, down, right, left functions)
            # Snake moves forward 10
            t.penup()
            t.forward(10)

            for i in range(len(segments)-1, 0, -1):   # Starting from end of array and going down
                # Previous segment's x and y coordinates
                x = segments[i-1].xcor()
                y = segments[i-1].ycor()
                segments[i].goto(x, y)   # Moving segment to previous segment's x and y coordinates

            # If there are segments, move the first segment to the snakes head
            if len(segments) > 0:  
                segments[0].goto(t.xcor(), t.ycor())

            if t.distance(apple) < 15:   # Snake has eaten apple(withing 15 of apple)
                apple.clear()   # Remove apple
                score += 10   # Increasing score
                pen.clear()   # Removing previous score
                pen.write("Score = {}".format(score), font=("Arial", 18), align="center")   # Writing new score
                
                # Setting and placing new apple on coordinates             
                x = random.randint(-310, 300)
                y = random.randint(-300, 310)
                apple.goto(x, y)

                # Creating new segment and adding to segments array
                segment = turtle.Turtle()
                segment.shape("square")
                segment.color("black")
                segment.penup()
                segments.append(segment)

            # Moving after 10ms and updating immediately after so no lag
            screen.ontimer(move, 10)
            screen.update()

    if t.xcor() <= boundary_left or t.xcor() >= boundary_right or t.ycor() <= boundary_down or t.ycor() >= boundary_forward:   # Snake is outside boundaries
        pen.penup() 
        pen.goto(0, 0)
        pen.write("GAME OVER!", font=('Courier', 30, 'italic'), align="center")   # Game over in center
            
# Forward function
def forward():
    global current_direction
    if t.ycor() < boundary_forward and current_direction != 270:   # y coordinate is valid and direction not down
        t.penup()
        t.setheading(90)
        current_direction = 90   # Updating going north

# Down function
def down():
    global current_direction
    if t.ycor() > boundary_down and current_direction != 90:   # y coordinate is valid and direction not up
        t.penup()
        t.setheading(270)
        current_direction = 270   # Updating going south

# Right function
def right():
    global current_direction
    if t.xcor() < boundary_right and current_direction != 180:   # x coordinate is valid and direction not right
        t.penup()
        t.setheading(0)
        current_direction = 0   # Updating going east

# Left function
def left():
    global current_direction
    if t.xcor() > boundary_left and current_direction != 0:   # x coordinate is valid and direction not left
        t.penup()
        t.setheading(180)  
        current_direction = 180   # Updating going west

# Listen for key press
screen.listen()

# Arrows control direction
screen.onkeypress(forward, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

# Moving snake
move()

# Screen don't disappear
turtle.done()