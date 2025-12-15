# Aaryan Gogna
# November 25, 2025
# Image Explorer Project

# Modules for the requirements of the project
import time
from PIL import Image

# Function to determine orange pixels that are a fire using certain rgb values
def is_orange(r, g, b):
    return (r >= 180 and 80 <= g <= 215 and b <= 130 and r > g)

# Function to determine white pixels that are a fire using certain rgb values
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


# Function that searches for a simple fire score based on input using Binary Search
def binary_search(sorted_list, target_score):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_score = sorted_list[mid][1]

        if mid_score == target_score:
            return mid 
        elif mid_score < target_score:
            high = mid - 1
        else:
            low = mid + 1

    return -1  


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

# Start the time for the program
program_start = time.time()


# Main loop to process each image
for filename in image_files:

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

    # Store results in the master list 
    fire_scores.append([filename, danger_score])

# End the time for the program and make a new variable to determine the time it took for the program to run
program_end = time.time()
total_time = program_end - program_start

# Start printing the output
print()
print("Final Fire Report:")
print()
print("All Fires and Their Scores:")
print()

# Print every fire in original order with its score and processing time
for entry in fire_scores:
    name = entry[0]
    score = entry[1]

    print(name + ": Danger Score " + str(score) + "/4")
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

print()
print("Total Processing Time for All Images: {:.3f} seconds".format(total_time))

print("You can search for fires with a danger score from 1 to 4.")
print()

# A while loop that makes sure a proper input is being entered.
while True:
    target = int(input("Enter a danger score to search for (1-4): "))
    
    if target < 1 or target > 4:
        print("No fires found with that score. Please enter a number between 1 and 4.")
        print()
    else:
        break


selection_sort(fire_scores)


index = binary_search(fire_scores, target)

if index != -1:
    result_name = fire_scores[index][0]
    result_score = fire_scores[index][1]
    print("Fire(s) with a score of " + str(target) + " was found: ")
else:
    print("No fire found with that score.")

print("\nAll fires with score " + str(target) + ":")
 
found_any = False
for entry in fire_scores:
    if entry[1] == target:
        print(" " + entry[0] + " (Score " + str(entry[1]) + "/4)")
        found_any = True

if not found_any:
    print("No other fires found with that score.")