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

# How to run the program:
1. Go to trinket.io/turtle and paste the code from the main.py file.
2. Run the code that you pasted.
3. Select a colour theme of your choice(Spring, Ocean, Sunset, Lavender, Rose, Night).
4. Select the speed of the animation of your choice(1-5).
5. Select the direction of your spiral of your choice(inward or outward).
6. Watch your spiral animate.
7. Lastly, view the details of your spiral, including colour theme, speed of the animation, direction of the animation, and the amount of recursive calls made.

# Screenshots of visual outputs (at least 2 different results):
I have attached both screenshots with different results in the "Screenshots_Outputs" folder in the "4.4" folder.
1. In "OutPut_1_Recursion.Assignment.png", you can see a "spring" themed spiral, the speed selected was "4", and the direction of the spiral was "inward".
2. In "Output_2_Recursive-Assignment.png", you can say an "ocean" themed spiral, the speed selected was "5", and the direction of the spiral was "outward".
 
# Test Cases
 1. For the first test case, I used the Spring color theme with a speed of 2 and selected the inward direction.
I expected the spiral to curl smoothly toward the center with bright green tones and a slow drawing speed.
When the program was run, the spiral appeared exactly as expected, it was centered and drew inward in a tight circular motion, and displayed the bright green spring color theme.
The speed was accurate, and the shrinking motion clearly showed recursion in action.
Overall, the actual output matched the expected result perfectly.
2. For the second test case, I used the Ocean color theme with a speed of 5 and selected the outward direction.
I expected the spiral to turn in the opposite direction, expanding outward instead of curling in, while showing smooth blue tones on a dark navy background.
When the program was run, the spiral expanded outward exactly as predicted, with fast animation and a clean outward curve.
The blue colors were clear, and the spiral movement confirmed that the turn_angle variable correctly controlled the direction.
There were no major differences between the expected and actual results in this test either.
3. For the third test case, I purposely entered invalid inputs to test the program’s error handling.
First, I typed an incorrect color theme that was not in the list, then entered a speed number that was out of range, and finally typed a random word instead of “inward” or “outward.”
I expected the program to reject each invalid entry and ask again until a valid input was given.
When tested, the program did exactly that, it repeatedly asked inputs like “Choose a Color Theme(Spring, Ocean, Sunset, Lavender, Rose, Night):” and “Choose drawing speed (1-5, 1 = slow, 3 = medium, 5 = fast): ” until the correct values were entered.
This confirmed that the program’s input validation works correctly and prevents crashes or invalid behavior.


# Discussion of reasonable recursion depth (why too low/high won't work):
1. The recursion depth in this program depends on the starting radius.
2. If it’s too low, the spiral ends quickly and looks incomplete.
3. If it’s too high, the program slows down or the spiral goes off-screen.
4. A radius around 120 is the best value, as it creates a full and proper looking spiral without it being too small or big.


