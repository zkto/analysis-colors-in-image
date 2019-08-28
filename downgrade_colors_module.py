import numpy as np


def make_downgrade(array):
    """ downgrade a color """
    new_array = list()
    for value in array:
        new_array.append(int(int(value /10) * 10))
    return new_array


def downgrade_colors(image_array):
    """ go through pixel matrix and downgrade colors """
    new_image_data = np.zeros((image_array.shape[0], image_array.shape[1], 4), dtype=np.uint8)
    for x in range(image_array.shape[0]):
        for y in range(image_array.shape[1]):
            new_image_data[x][y] = make_downgrade(image_array[x][y])
    return new_image_data
