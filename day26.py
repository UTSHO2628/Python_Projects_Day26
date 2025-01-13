import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Firework Show")

# Create a turtle for drawing fireworks
firework = turtle.Turtle()
firework.speed(0)
firework.hideturtle()

# Function to draw a firework
def draw_firework(x, y):
    colors = ["red", "blue", "yellow", "green", "purple", "orange", "white"]
    firework.penup()
    firework.goto(x, y)
    firework.pendown()
    for _ in range(36):
        firework.color(random.choice(colors))
        firework.forward(100)
        firework.right(170)

# Function to create random fireworks
def create_fireworks():
    for _ in range(10):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        draw_firework(x, y)

# Run the firework show
create_fireworks()

# Keep the window open until clicked
screen.exitonclick()