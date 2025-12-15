"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you’ve made yourself 
"""
# Aaryan Gogna
# October 15, 2025
# Drawing with Turtle

import turtle

aaryan = turtle.Turtle()
aaryan.speed(1)
aaryan.color("darkblue", "lightblue")


def draw_square(side_length=100):
    for mrChin in range(4):
        aaryan.forward(side_length)
        aaryan.left(90)

def draw_rectangle(length=200, width=100):
    for mrChin in range(2):
        aaryan.forward(length)
        aaryan.right(90)
        aaryan.forward(width)
        aaryan.right(90)

def draw_triangle(side_length=100):
    for mrChin in range(3):
        aaryan.forward(side_length)
        aaryan.left(120)

def draw_circle(radius=100):
    aaryan.circle(radius)
    
def draw_octagon(side_length=100, turn_angle=360/8):
    for mrChin in range(8):
        aaryan.forward(side_length)
        aaryan.left(turn_angle)

def draw_star():
    for mrChin in range(5):
        aaryan.forward(100)
        aaryan.right(144)


while True:
    response = input("What shape would you like to draw (square, rectangle, triangle, circle, octagon, star)? Type 'exit' to stop: ").lower().strip()

    if response == "exit":
        break

    aaryan.begin_fill()

    if response == "square":
        draw_square()
    elif response == "rectangle":
        draw_rectangle()
    elif response == "triangle":
        draw_triangle()
    elif response == "circle":
        draw_circle()
    elif response == "octagon":
        draw_octagon()
    elif response == "star":
        draw_star()
    else:
        print("That shape isn't recognized!")

    aaryan.end_fill()

turtle.done()
