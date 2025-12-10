# Aaryan Gogna
# November 25, 2025
# Image Explorer Project

# Modules for the requirements of the project
import time
from PIL import Image

# Function to determine orange pixels that are a fire
def is_orange(r, g, b):
    return (r >= 180 and 80 <= g <= 215 and b <= 130 and r > g)

# Function to determine white pixels that are a fire
def is_white(r, g, b):
    return (r >= 210 and g >= 210 and b >= 180)

# Function that sorts fire scores from highest to lowest using Selection Sort
def selection_sort(score_list):
    for i in range(len(score_list)):
        max_index = i
        for j in range(i + 1, len(score_list)):
            if score_list[j][1] > score_list[max_index][1]:
                max_index = j
        score_list[i], score_list[max_index] = score_list[max_index], score_list[i]

# List of image names in a list, this will be used in a loop to read through each image
image_files = [
    "BonFire",
    "BurningMatch",
    "BushFire",
    "CampFire",
    "CandleFlame",
    "FireExplosion",
    "FirePlace",
    "ForestFire",
    "HouseFire",
    "WildFireSmoke"
]

# Master list to store each image name and a fire score
fire_scores = []

# Dictionary to store processing times for each image
processing_times = {}

# Main loop to process each image
for filename in image_files:

    # Start the time so we can determine the time it takes to process each image
    start_time = time.time()

    # This will open every file in the 6.7/images folder
    file = Image.open("6.7/Images/" + filename + ".jpg")
    img = file.load()

    width = file.width
    height = file.height

    # Initialize two variables which will eventually lead to my final output
    orange_pixels = 0
    white_pixels = 0

    # Nested for loop that goes through every single pixel in every file
    for i in range(width):
        for j in range(height):

            r = img[i, j][0]
            g = img[i, j][1]
            b = img[i, j][2]

            # While the image is being processed the program will process each pixel.
            # It will look at the conditions I made, if the condition matches the RGB values,
            # then the pixel variable I made will increase by one, depending on which RGB values it matches.
            if is_orange(r, g, b):
                orange_pixels += 1
            if is_white(r, g, b):
                white_pixels += 1

    # Converts all pixels into percentages in a multi step conversion
    total_pixels = width * height
    orange_percent = 100 * orange_pixels / total_pixels
    white_percent = 100 * white_pixels / total_pixels

    # This is the fire percent score, it then converts into a fire intensity score
    fire_percent = int(white_percent) + int(orange_percent)

    # Conditional statements that classify the danger score based on fire percentage
    if fire_percent < 6:
        danger_score = 1
    elif fire_percent < 16:
        danger_score = 2
    elif fire_percent < 31:
        danger_score = 3
    else:
        danger_score = 4

    # End the timing
    end_time = time.time()
    elapsed = end_time - start_time

    # Store results in the master list and in the processing time dictionary
    fire_scores.append([filename, danger_score])
    processing_times[filename] = elapsed


# Start printing the output
print("Final Fire Report:")
print()
print("All Fires and Their Scores:")
print()

# Print every fire in original order with its score and processing time
for entry in fire_scores:
    name = entry[0]
    score = entry[1]
    time_taken = processing_times[name]

    print(name + ": Danger Score " + str(score) + "/4")
    print("Processing Time: " + str(round(time_taken, 3)) + " seconds")
    print()

# Sort the results from highest to lowest danger score
selection_sort(fire_scores)

print("Top 5 Most Intense Fires:")
print()

# Get the first 5 elements from the sorted list
top5 = fire_scores[:5]

# Initialize a variable to repeat it 5 times
rank = 1

# A for loop that displays the danger score of the fires, it loops through the first and second values of each element
for entry in top5:
    name = entry[0]
    score = entry[1]
    print(str(rank) + ". " + name + " - Score " + str(score) + "/4")
    rank += 1
