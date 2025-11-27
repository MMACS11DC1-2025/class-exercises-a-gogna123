# Aaryan Gogna
# Novemeber 25, 2025
# Image Explorer Project

from PIL import Image

def is_orange(r, g, b):
    return (r > 170 and g > 80 and r > g and b < 120)

def is_white(r, g, b):
    return (r > 220 and g > 210 and b > 150)


image_files = [
    "6.7/Images/BonFire.jpg",
    "6.7/Images/BurningMatch.jpg",
    "6.7/Images/BushFire.jpg",
    "6.7/Images/CampFire.jpg",
    "6.7/Images/CandleFlame.jpg",
    "6.7/Images/FireExplosion.jpg",
    "6.7/Images/FirePlace.jpg",
    "6.7/Images/ForestFire.jpg",
    "6.7/Images/HouseFire.jpg",
    "6.7/Images/WildFireSmoke.jpg"
]

for filename in image_files:

    file = Image.open(filename)
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

    print("Orange: {:.3f}%".format(orange_percent))
    print("White: {:.3f}%".format(white_percent))
    print()  

