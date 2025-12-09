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

