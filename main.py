import turtle
import random
import sys
from datetime import datetime

# Set up the screen
screen = turtle.Screen()
screen.title("Colorful Turtle Art")
screen.bgcolor("black")
screen.colormode(255)  # Allow RGB values between 0-255

# Create turtle
tom = turtle.Turtle()
tom.speed(0)  # Maximum speed for faster drawing
tom.pensize(5)
tom.shape("turtle")

i = 72

print("\nProcess START: " + str(datetime.now()))

# Function to exit on click
def exit_on_click(x, y):
    print("\nProcess ENDED by user at: " + str(datetime.now()))
    turtle.bye()

# Draw pattern
for x in range(4):
    for j in range(i):
        # Random pen color (valid RGB values: 0-255)
        myPenColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tom.pencolor(myPenColor)



        # Move and rotate
        tom.forward(250 - j * 0.5)  # Spiral effect by reducing step size
        tom.right(85)

    tom.left(90)

# Hide turtle if visible
if tom.isvisible():
    tom.hideturtle()

print("Process END: " + str(datetime.now()))
print("Click on the window to exit the program.")

# Exit on click
screen.onclick(exit_on_click)

# Keep the window open
turtle.mainloop()
