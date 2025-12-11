from PIL import Image

def is_green(r,g,b):
    if r >= 0 and r <= 100 and g >= 200 and g <= 255 and b >= 0 and b <= 100:
        return "green"
    else:
        return "not green"
image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

image_output = Image.open("5.1/kid-green.jpg")

width = image_output.width
height = image_output.height
for i in range(width):
    for j in range(height):
        im_r = image_green[i,j][0]
        im_g = image_green[i,j][1]
        im_b = image_green[i,j][2]

        if is_green(im_r, im_g, im_b) == "green":
            beach = image_beach[i,j]
            xy = (i,j)
            image_output.putpixel(xy, beach)
image_output.save("output.png","png")

# Question 1
"""def islight(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    average = int((r + g + b) / 3)

    if average >= 128:
        return True
    else:
        return False
    
print(islight((500, 0, 0)))"""

# Question 2 







