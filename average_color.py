from scipy import misc
import sys
import numpy as np
from PIL import Image

"""This module calculate the green percentage color"""

print(sys.argv)

if len(sys.argv) == 2:
    name_file = sys.argv[1]
else:
    name_file = 'datasets/DJI_0038.png'
arr_image = misc.imread(name_file)
q_pixels = 0
q_green = 0

# new matrix
h = arr_image.shape[0]
w = arr_image.shape[1]
new_data = np.zeros((h, w, 4), dtype=np.uint8)

# count green pixels
for x in range(arr_image.shape[0]):
    for y in range(arr_image.shape[1]):
        q_pixels +=1
        arr_temp = arr_image[x][y]
        if (int(arr_temp[1]) > 30 and
                int(arr_temp[1]) != 0 and int(arr_temp[2]) != 0 and
                float(arr_temp[0]) / float(arr_temp[1]) < 0.85 and
                float(arr_temp[2]) / float(arr_temp[1]) < 0.5):
            q_green += 1
            new_data[x][y] = [255, 255, 255, 255]
        else:
            new_data[x][y] = [0, 0, 0, 255]


p_average = (q_green/q_pixels)*100

print("File analyzed {0}".format(name_file))
print("Dimension of the image {0}".format(arr_image.shape))
print("Pixel quantity {0}".format(q_pixels))
print("Green pixel quantity {0}".format(q_green))
print("Green percentage in the image {0}".format(p_average))


print("create new file")
img = Image.fromarray(new_data)
img.save(name_file.replace(".png", "_BOOL.png"))