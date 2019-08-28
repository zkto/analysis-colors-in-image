
def get_data_csv(file):
    """ Return two lists
     one of color and other for the quantity"""
    color_array = list()
    color_quantity = list()
    f = open(file, "r")
    lines_content = f.readlines()
    for line in lines_content:
        color, q = line.split(";")
        color_array.append(color.strip())
        color_quantity.append(q.strip())
    return color_array, color_quantity


def convert_to_rgb(array):
    """ Return a list with the colors in rgb format """
    new_list = list()
    for element in array:
        new_list.append("rgb({0},{1},{2})".format(element[0], element[1], element[2]))
    return new_list


def cast_int_list(array):
    """ Cast all strings elements
    of list in int"""
    new_list = list()
    for element in array:
        new_list.append(int(element))
    return new_list


def unpack_array(array):
    """" unpack color list in four lists """
    arr_r = list()
    arr_g = list()
    arr_b = list()
    arr_rgb = list()
    for element in array:
        arr_temp = element.replace("[", "").replace("]", "").replace(" ", "").split(",")
        arr_r.append(arr_temp[0])
        arr_g.append(arr_temp[1])
        arr_b.append(arr_temp[2])
        arr_rgb.append(arr_temp[:3])
    return arr_r, arr_g, arr_b, arr_rgb


def unpack_array_green(array, q_colors):
    """ Unpack only the green colors in four lists """
    arr_r = list()
    arr_g = list()
    arr_b = list()
    arr_rgb = list()
    arr_q = list()
    for index, element in enumerate(array):
        arr_temp = element.replace("[", "").replace("]", "").replace(" ", "").split(",")
        if (int(arr_temp[1]) > 30 and int(arr_temp[2]) != 0 and
                float(arr_temp[0])/float(arr_temp[1]) < 0.85 and
                float(arr_temp[2])/float(arr_temp[1]) < 0.5):
            arr_r.append(arr_temp[0])
            arr_g.append(arr_temp[1])
            arr_b.append(arr_temp[2])
            arr_rgb.append(arr_temp[:3])
            arr_q.append(q_colors[index])
    return arr_r, arr_g, arr_b, arr_rgb, arr_q


def unpack_array_gray(array, q_colors):
    """ Unpack only the green colors in four lists """
    arr1 = list()
    arr2 = list()
    arr3 = list()
    arr4 = list()
    arr_q = list()
    for index, element in enumerate(array):
        arr_temp = element.replace("[", "").replace("]", "").replace(" ", "").split(",")
        if (abs(int(arr_temp[0]) - int(arr_temp[1])) < 20 and
                abs(int(arr_temp[1]) - int(arr_temp[2])) < 20 and
                abs(int(arr_temp[0]) - int(arr_temp[2])) < 20 ):
            arr1.append(arr_temp[0])
            arr2.append(arr_temp[1])
            arr3.append(arr_temp[2])
            arr4.append(arr_temp[:3])
            arr_q.append(q_colors[index])
    return arr1, arr2, arr3, arr4, arr_q
