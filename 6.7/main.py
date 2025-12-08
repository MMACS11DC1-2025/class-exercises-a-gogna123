# Aaryan Gogna
# November 25, 2025
# Image Explorer Project

import time
from PIL import Image

def is_orange(r, g, b):
    return (r >= 180 and 80 <= g <= 215 and b <= 130 and r > g)

def is_white(r, g, b):
    return (r >= 210 and g >= 210 and b >= 180)


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

for filename in image_files:

    start_time = time.time()

    file = Image.open("6.7/Images/" + filename + ".jpg")
    img = file.load()

    width = file.width
    height = file.height

    orange_pixels = 0
    white_pixels = 0

    for i in range(width):
        for j in range(height):

            r = img[i, j][0]
            g = img[i, j][1]
            b = img[i, j][2]

            if is_orange(r, g, b):
                orange_pixels += 1
            if is_white(r, g, b):
                white_pixels += 1

    total_pixels = width * height
    orange_percent = 100 * orange_pixels / total_pixels
    white_percent = 100 * white_pixels / total_pixels
    fire_percent = int(white_percent) + int(orange_percent)

    if fire_percent < 6:
        size = "SMALL Fire. Proceed with caution!"
    elif fire_percent < 16:
        size = "MEDIUM Fire. Don't approach without professionals!"
    elif fire_percent < 31:
        size = "LARGE Fire. Get yourself out of that place!"
    else:
        size = "EXTREME Fire. Stay OUT!"

    
    end_time = time.time()
    elapsed = end_time - start_time

    print(filename + ":")
    print(size)
    print("Processing Time: {:.3f} seconds".format(elapsed))
    print()  

