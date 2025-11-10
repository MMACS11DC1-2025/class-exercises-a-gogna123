# Recursive Spiral
# Aaryan Gogna
# October 27, 2025

# Import the turtle to start the animation
import turtle

# Dictionary of available color options for the spiral
Spiral_Themes = {
    "spring":  {"PenColours": "#00FF9C", "BackgroundColours": "#002B1F"},
    "ocean":   {"PenColours": "#33A1FF", "BackgroundColours": "#001933"},
    "sunset":  {"PenColours": "#FF8C42", "BackgroundColours": "#1A0B00"},
    "lavender":{"PenColours": "#CBA6F7", "BackgroundColours": "#1C0F24"},
    "rose":    {"PenColours": "#FF4D6D", "BackgroundColours": "#19000A"},
    "night":   {"PenColours": "#89CFF0", "BackgroundColours": "#0A0F1A"}
}

# Function that fills the background color of the spiral
def paint_background(color):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.dot(2500, color)
    turtle.pendown()

# Function that draws the spiral recursively and counts total recursive calls
def draw_spiral(radius, turn_angle):
    if radius <= 1:
        return 0
    turtle.circle(radius, turn_angle)
    count = draw_spiral(radius - 1, turn_angle)
    return count + 1

print("Welcome to the Recursive Spiral!")
print("Themes Available: Spring, Ocean, Sunset, Lavender, Rose, Night\n")

# Choose Theme by asking the user for the theme choice
while True:
    theme_choice = input("Choose a Colour Theme(Spring, Ocean, Sunset, Lavender, Rose, Night): ").strip().lower()
    if theme_choice in Spiral_Themes:
        break
    print("That theme doesn’t exist. Try again.\n")

# Choose Speed by asking the user for the speed choice
while True:
    speed_input = input("Choose drawing speed (1-5, 1 = slow, 3 = medium, 5 = fast): ").strip()
    if speed_input.isdigit():
        speed = int(speed_input)
        if 1 <= speed <= 5:
            break
    print("Please enter a number between 1 and 5.\n")

# Choose Direction of Spiral by asking the user for the direction
while True:
    direction = input("Choose Spiral direction (Inward/Outward): ").strip().lower()
    if direction in ["inward", "outward"]:
        break
    print("please type 'Inward' or 'Outward'.\n")

# Set the direction of the turn based on user input of the "Direction of the Spiral"
if direction == "outward":
    turn_angle = -45
else:
    turn_angle = 45

# Setup the turtle settings
turtle.speed(speed * 2)
turtle.pensize(3)
paint_background(Spiral_Themes[theme_choice]["BackgroundColours"])
turtle.pencolor(Spiral_Themes[theme_choice]["PenColours"])

# Starting position for the turtle
turtle.penup()
turtle.goto(0, -100)  
turtle.pendown()
starting_radius = 120

print("\nDrawing your Perfect Spiral... please wait!\n")
total_calls = draw_spiral(starting_radius, turn_angle)

# Final Message including amount of recursive calls made
print("\nSpiral Complete!")
print("Theme Chosen: " + theme_choice)
print("Speed Selected: " + str(speed))
print("Direction: " + direction)
print("Total Recursive Calls Made: " + str(total_calls))
print("Enjoy your Recursive Spiral!")


turtle.done()
