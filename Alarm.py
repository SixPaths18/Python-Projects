import turtle, winsound, threading
from datetime import datetime

screen = turtle.Screen()
t = turtle.Turtle()
circle = turtle.Turtle()

# Setting up screen   
screen.title("Alarm Clock")
screen.setup(960, 640)
screen.bgcolor("black")

# Setting tracer to 0 to turn off auto updates
screen.tracer(0)

# Setting up t
t.hideturtle()
t.goto(0, 0)
t.color("white")

# Array storing alarm times
times = []

# Stopping pause of clock
def ring_beep():
    def play():
        for _ in range(1):
            winsound.Beep(600, 3000)
    threading.Thread(target=play).start()

# Function detecting time to ring
def ring():
    global hh, mm, now

    # Current time
    now = datetime.now()
    hh = now.hour
    mm = now.minute
    ss = now.second

    # Checking if time is reached
    for alarm in times:
        if alarm[0] == hh and alarm[1] == mm and ss == 0:
            ring_beep()

# Writing time
def write():
    # Getting time
    now = datetime.now()

    # Current hour, minute and seconds
    hh = now.hour
    mm = now.minute
    ss = now.second

    # Clearing and updating time evry 1s (1000ms)
    t.clear()
    t.write("{:02d}:{:02d}:{:02d}".format(hh, mm, ss),  align="center", font=("Arial", 100, "bold"))

    ring()

    screen.ontimer(write, 1000)

write()

# Drawing circle
circle.penup()
circle.goto(0, -120)
circle.shape("circle")
circle.shapesize(4)
circle.color("grey")
circle.stamp()

# Drawing plus sign on circle
circle.hideturtle()
circle.goto(0, -190)
circle.color("white")
circle.write("+", align="center", font=("Arial", 90, "normal"))

screen.update()

# Function to detect click on circle
def click(x, y):
    global hour, minute
    if (x-0)**2 + (y+120)**2 <= 40**2:
        # Input and validate hour
        hour = screen.textinput("Add alarm", "Enter hour:")
        if hour is None:
            return

        while not hour.isdigit() or int(hour) < 0 or int(hour) > 23:
            hour = screen.textinput("Add Alarm", "Invalid! Enter hour:")

        # Input and validate minute
        minute = screen.textinput("Add alarm", "Enter minute:")
        if minute is None:
            return

        while not minute.isdigit() or int(minute) < 0 or int(minute) > 59:
            minute = screen.textinput("Add Alarm", "Invalid! Enter minute:")

        # Storing time in array
        times.append([int(hour), int(minute)])

screen.onscreenclick(click)

turtle.mainloop()