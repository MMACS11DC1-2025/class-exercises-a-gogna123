# Project Overview:
The theme of my Image Explorer project is fire detection and fire danger analysis.
My program analyzes a set of 10 fire-related images, including bonfires, forest fires, house fires, and explosions, to estimate how dangerous each fire is. This has real-world applications in wildfire monitoring, emergency response, and fire safety awareness. I have also added a personal self evaluation in the "6.7" folder, I am not biased about my work, I am just evaluating my work honestly and fairly, the self evaluation I give myself is what I believe I deserve on this project. I am not influencing you on your marking for the self evaluation.

# Visual Feature Detection:
The visual feature my program detects is fire-colored pixels, specifically orange and white pixels.
    Orange pixels represent flames.
    White pixels represent extremely hot or intense fire areas, such as explosions or very bright flames.

To detect these features, I created two functions:
    is_orange(r, g, b)
    is_white(r, g, b)

Each function checks whether a pixel’s RGB values fall within a realistic range for fire colors. If a pixel matches one of these conditions, it is counted as part of the fire.

# Testing and Validation:
To make sure my program works correctly, I tested it in multiple stages as I built it.

First, I tested the pixel detection functions (is_orange and is_white) by printing the percentage of detected pixels for each image and checking if the values made sense visually. For example, images with large forest fires or explosions produced higher fire scores, while small fires like candles or matches produced lower scores.

Next, I tested the danger score system by adjusting the original values and comparing the outputs(1–4) to how intense each fire looked in the image. This helped confirm that the scoring system was reasonable and consistent.

I also tested the Selection Sort algorithm by printing the list before and after sorting to verify that fires were ordered correctly from highest to lowest danger score. The top 5 list was checked to make sure it always showed the most intense fires.

Finally, I tested the Binary Search feature using multiple input values (1, 2, 3, and 4). I confirmed that:
The program correctly found fires when a matching danger score existed.
The program displayed a clear message when no fires matched the searched score.
Through this testing process, I verified that each part of the program worked as intended before moving on to the next feature.

# Performance Analysis:
To analyze the performance of my program, I used Python’s time module to measure how long the program took to process all images combined. The timer starts before the image-processing loop begins and stops after all images have been analyzed.

The program reports the total processing time in seconds, formatted to three decimal places. This makes the output clean and easy to read while still being precise.

Most of the processing time is spent inside the nested loops that go through every pixel of every image. This makes sense because each image contains thousands of pixels, and every pixel must be checked to see if it matches the fire detection rules. The Selection Sort and Binary Search algorithms run very quickly in comparison because they only work on a small list of image scores.

Overall, the program performs efficiently for the number of images used, and the timing results clearly show where most of the work is being done.

# Challenges Faced During the Process:
1. One major challenge I faced was while implementing Binary Search. At first, I accidentally used / 2 instead of // 2 when calculating the middle index of the list. This caused an error because / returns a decimal number, and list indexes must be whole numbers.

It took me some time to understand why the program was not working correctly, even though the logic seemed right. After reviewing how Binary Search works and learning the difference between regular division and integer division in Python, I realized that I needed to use // 2 to always get an integer index.

Once I fixed this mistake, Binary Search worked exactly as expected. This challenge helped me better understand Python data types and why small syntax details can have a big impact on how an algorithm behaves. It also taught me to carefully debug step by step instead of assuming the logic is wrong.

2. Another challenge I faced was making sure that Binary Search worked correctly on my fire_scores list. Binary Search only works properly if the list is already sorted in the correct order. At one point, I was testing the search before sorting the list, which caused incorrect or inconsistent results.

To fix this, I ensured that the selection_sort() function was always called before running Binary Search. This guaranteed that the list was ordered from highest danger score to lowest, allowing Binary Search to function correctly.

This challenge helped me understand that algorithms often depend on specific preconditions, and even a correctly written algorithm can fail if those conditions are not met. It reinforced the importance of execution order and algorithm design.

# Test Cases:
I have attached screenshots of the outputs as proof everything is working in the "6.7" folder.
1. For the first test case, I inputted the number 3 so I can see which fires have a score of 3.
I expected the program to print to the screen the fires with the score of 3.
When the program was run, the program did exactly what I expected.

2. For the second test case, I purposely entered invalid inputs to test the program’s error handling.
I typed an incorrect number that was not in the danger score.
I expected the program to not let the input go through ask again until a valid input was given.
When I entered an invalid input, it repeatedly asked the inputs "No fires found with that score. Please enter a number between 1 and 4,"Enter a danger score to search for (1-4):" until a valid input value was entered.
This confirmed that the program’s input validation works correctly and prevents crashes or invalid behavior.

# Real-World Importance and Creativity:
Fire detection and fire danger analysis is important in the real world because fires, especially wildfires, can cause serious damage to people, homes, and the environment. This project shows how image analysis can be used to estimate how dangerous a fire is by examining visual features such as flame color and brightness. Similar techniques are used in real systems that analyze satellite images, drones, or security cameras to help detect fires early and assess their severity. I chose this theme because it connects computer science to public safety and environmental protection, and it demonstrates how simple algorithms like sorting and searching can turn raw image data into useful information that could help emergency responders make faster and better decisions. My program is much similar to NASA's wildfire monitoring system, but is way less advanced.


# Day 1
Today I chose my project theme: analyzing fire images to estimate the size of a fire.
1. I added 10 fire-related images into the 6.7/Images folder, including bonfires, forest fires, house fires, and explosions.
2. I wrote the first version of the program, which loads each image and calculates the percentage of orange pixels and white pixels. 
3. This will later determine how large the fire is. I also worked on accurately using rgb values to get the best results.
4. By the end of today, the program was successfully printing the orange and white pixel percentages for every image.

# Day 2 plan:
1. Combine orange + white percentages into one “fire intensity score”
2. Create if-statements to label each fire as Small, Medium, Large, or Extreme

# Day 2:
Today I did small singular steps to get closer and closer to my final result which will display a statistic. I also included a time function to determine the amount of time the program took to process each image.
1. On day 1, I was just displaying the percents of the fire and orange pixels. Now, I made a new variable called "fire_percent"
which added all the white and orange pixels together.
2. I then made conditional statements, based on the percentage of the fire, I asked CHATGPT what would be a good observation based on my outputs.
3. I also added a time function that lets the user know the time it takes for each image thats processed.
4. Overall, day 2 was a success.

# Day 3 Plan:
1. Create a list that stores each images name and percent score used the append feature.
2. Print the list for testing.

# Day 3:
Today I created a master list that stores each image’s name and its fire intensity score.
1. After calculating the orange and white pixel percentages for every image, I combined them into one value and used the .append() function to add ["ImageName", score] into a list called fire_scores.
2. I printed the list at the end of the program to make sure everything was working correctly.
3. This prepares the project for sorting and searching in the next stages.

# Day 4 Plan:
1. Write the Selection Sort function that sorts the fire_scores list from highest fire score to lowest.
2. Print the top 5 most intense fires using list slicing.
3. Test that the sorting works correctly before moving on.

# Day 4:
Today I added pseudo comments to my code, added a selection_sort function that sorts the fire and danger score. This was a small but important step in getting the project closer to completion.
1. I wrote a Selection Sort function that sorts all fires from highest danger score to lowest. 
2. After the sorting was complete, I generated a final report that displays all fires, their danger scores, and their processing times.
3. Todays selection sort will help me implement binary search tomorrow.

# Day 5 Plan:
1. Create a Binary Search function that searches the sorted fire list for a specific danger score (1, 2, 3, or 4).
2. Ask the user for a danger score they want to search for (ex: "Find all fires with a score of 3").
3. Use Binary Search to locate one matching fire score in the sorted list.
4. If a match is found, display the fire’s name and score.
5. If no match is found, print a simple message like “No fire found with that score.”
6. Test the Binary Search with multiple target values to make sure it works.

# Day 5:
Today I implemented the Binary Search feature for my fire detection program. Before starting Binary Search, I also changed my time-tracking system so that the program now measures one total processing time instead of timing each image individually. This keeps the output cleaner and still shows the overall performance of the program. Overall, I'm almost done the project!
1. First, I wrote a Binary Search function that looks through the sorted fire list and searches for a specific danger score (1–4).
2. I added user input so the program asks the user which danger score they want to find.
3. Binary Search is then used to locate one matching fire inside the sorted list.
4. If at least one fire has that score, the program prints a message saying a match was found.
5. After that, I also added a feature that lists all fires with that danger score (not just the first result).
6. If no fires match the score, the program prints a simple message explaining that no results were found.
7. I tested Binary Search with several numbers (1, 2, 3, and 4), and the program showed the correct results each time.

# Day 6 Plan:
1. Add pseudocode to all my major components of my code.
2. Project Overview.
3. Testing with test cases.
4. Performace analysis.
5. Challenges faced and how I overachieved them.
6. Creativity section, why fire detection is important to society.

# Day 6:
Today was basically the final day of the project, I focused by reviewing my code for the upcoming test, improving documentation to show my understanding, and reviewing the rubric to make sure all requirements were fully met.
1. I added pseudocode for clarity in major components of the code.
2. Completed project overview, testing and validation, performance analysis, challenges faced, and creativity sections.
3. I improved the user input by adding a while loop that prevents wrong inputs from being entered.

# Day 7 Plan:
1. Add self rubric evaluation to the folder.
2. Add screenshots of testing outputs.
3. Review all code from main.py and readme.md to make sure that everything is done in the project.md.

# Day 7:
Today is the final day of the project. I had alot of fun using my ideas and implementing them!
1. I added test cases screenshots in the "6.7" folder.
2. I added a self evaluation in the "6.7" folder.

