import time
t0 = time.time()
from PIL import Image
t1 = time.time()
file = Image.open("5.5/blue.jpg")
jbimg = file.load()

# Go through all the pixels in the image
width = file.width
height = file.height

# Initialize a counter

blue_pixels = 0
t2 = time.time()
for i in range(width):
    for j in range(height):
            r = jbimg [i, j] [0]
            g = jbimg [i, j] [1]
            b = jbimg[i, j] [2]

            if b > r and b > g:
                blue_pixels += 1
t3 = time.time()

percent_blue = 100*blue_pixels/(width*height)

print(percent_blue)

if percent_blue < 30.00:
     print("This image is not that blue")

else:
     print("This image is blue!")

# Calculate and output elapsed times
module_load = t1-t0
image_open_load = t2-t1
loop = t3-t2
entire = t3-t0

timings = "It took {:.3f}s to import PIL, {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(module_load, image_open_load, loop, entire)
print(timings)