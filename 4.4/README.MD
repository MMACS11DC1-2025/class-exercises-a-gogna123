# Project Overview:
This Recursive Spiral can create a smooth and shrinking spiral design, based on recursion and what we learned in Python Turtle.
The user thats using this Recursive Spiral can select a color theme, drawing speed (1–5), and spiral direction (inward or outward).
Each time the program runs, it produces a unique and colourful pattern that shows recursion was used for this spiral.

# Explanation of your recursive approach and why it works:
1. The spiral is drawn using a recursive function called draw_spiral(radius, turn_angle).
2. Each time the function runs, it draws one curved part of the spiral using the Turtle circle() command.
3. Then it makes a recursive call to draw another spiral that is slightly smaller by reducing the radius.
4. This keeps happening until the radius gets very small, which is when the base case stops the recursion.
5. This is the base case "if radius <= 1:
                             return 0"
6. This prevents the spiral from going on forever.
7. The function also returns a value each time to count how many recursive calls were made in total.
8. This shows how recursion works step by step, the same function keeps calling itself, solving a smaller version of the problem each time, until it reaches the end.



