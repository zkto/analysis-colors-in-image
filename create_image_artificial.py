from PIL import Image
import numpy as np
import ast
import random
import datetime

from graphic_csv_colors import unpack_array_green, get_data_csv

SIZEZONEA = 100
SIZEZONEB = 50
SIZEZONEC = 200


def generale_color_list(file):
        color_array = list()
        f = open(file, "r")
        lines_content = f.readlines()
        for line in lines_content:
            color, q = line.split(";")
            for i in range(int(q.strip())):
                color_array.append(ast.literal_eval(color.strip()))
        return color_array


def generale_color_list_gray(file):
    color_array = list()
    f = open(file, "r")
    lines_content = f.readlines()
    for line in lines_content:
        color, q = line.split(";")
        arr_temp = color.replace("[", "").replace("]", "").replace(" ", "").split(",")
        if (abs(int(arr_temp[0]) - int(arr_temp[1])) < 20 and
                abs(int(arr_temp[1]) - int(arr_temp[2])) < 20 and
                abs(int(arr_temp[0]) - int(arr_temp[2])) < 20 ):
            for i in range(int(q.strip())):
                color_array.append(ast.literal_eval(color.strip()))
    return color_array


def generale_color_list_green(file):
    color_array = list()
    f = open(file, "r")
    lines_content = f.readlines()
    for line in lines_content:
        color, q = line.split(";")
        arr_temp = color.replace("[", "").replace("]", "").replace(" ", "").split(",")
        if (int(arr_temp[1]) > 30 and
                int(arr_temp[1]) != 0 and
                float(arr_temp[0]) / float(arr_temp[1]) < 0.85 and
                float(arr_temp[2]) / float(arr_temp[1]) < 0.5):
            for i in range(int(q.strip())):
                color_array.append(ast.literal_eval(color.strip()))
    return color_array


def initialize_matrix_color(w , h, color_list):
    data = np.zeros((h, w, 4), dtype=np.uint8)
    for x in range(h):
        for y in range(w):
            data[x,y] = color_list
    return data


def create_matrix_color(w, h, color_list):
    random_up = len(color_list)
    data = np.zeros((h, w, 4), dtype=np.uint8)
    for x in range(h):
        for y in range(w):
            index = random.randint(0, random_up - 1)
            data[x, y] = color_list[index]
    return data


def make_trees(array, color_list, dimension,p):
    print("Generating trees of size {0} pixels, with the {1}% percent likely to appear".format(dimension, p))
    random_up = len(color_list)
    for x in range(0, array.shape[0], dimension):
        for y in range(0, array.shape[1], dimension):
            index = random.randint(0, random_up - 1)
            middle_x, middle_y = int(x + dimension/2), int(y + dimension/2)
            if middle_x < array.shape[0] and middle_y < array.shape[1]: # section in the range
                array[middle_x, middle_y] = color_list[index]
                random_visible = random.randint(0, 99)
                if random_visible in range(p):
                    tope_norte=dimension-20
                    diferencia_inicial = 1
                    for i in range(int(x+ dimension/2), x, -1):  # painting in north way
                        if (tope_norte - diferencia_inicial ) > 0:
                            tope_norte = random.randint(tope_norte-diferencia_inicial, tope_norte - 1)
                            margen_norte = int((dimension-tope_norte)/2)
                            if i % 3 == 0:
                                diferencia_inicial += 1
                            for k in range(y+margen_norte,y+margen_norte+tope_norte ):
                                index = random.randint(0, random_up - 1)
                                if i < array.shape[0] and k < array.shape[1]:
                                    array[i, k] = color_list[index]
                        else:
                            break
                    tope_sur = dimension-20
                    diferencia_inicial = 1
                    for i in range(int(x+dimension/2), x+dimension):  # painting in north way
                        if (tope_sur - diferencia_inicial ) > 0:
                            tope_sur = random.randint(tope_sur-diferencia_inicial, tope_sur - 1)
                            margen_sur = int((dimension - tope_sur) / 2)
                            if i % 3 ==0:
                                diferencia_inicial += 1
                            for k in range(y + margen_sur, y + margen_sur + tope_sur):
                                index = random.randint(0, random_up - 1)
                                if i < array.shape[0] and k < array.shape[1]:
                                    array[i, k] = color_list[index]
                        else:
                            break

                    tope_oeste = dimension -20
                    diferencia_inicial = 1
                    for k in range(int(y+dimension/2), y, -1):  # painting in west way
                        if (tope_oeste - diferencia_inicial ) > 0:
                            tope_oeste = random.randint(tope_oeste - diferencia_inicial, tope_oeste - 1)
                            margen_oeste = int((dimension - tope_oeste) / 2)
                            if k % 3 == 0:
                                diferencia_inicial += 1
                            for i in range(x + margen_oeste, x + margen_oeste + tope_oeste):
                                index = random.randint(0, random_up - 1)
                                if i < array.shape[0] and k < array.shape[1]:
                                    array[i, k] = color_list[index]
                        else:
                            break
                    tope_este = dimension-20
                    diferencia_inicial = 1
                    for k in range(int(y+dimension/2), y+dimension):  # painting in east way
                        if (tope_este - diferencia_inicial ) > 0:
                            tope_este = random.randint(tope_este - diferencia_inicial, tope_este - 1)
                            margen_este = int((dimension - tope_este) / 2)
                            if k % 3 == 0:
                                diferencia_inicial += 1
                            for i in range(x + margen_este, x + margen_este + tope_este):
                                index = random.randint(0, random_up - 1)
                                if i < array.shape[0] and k < array.shape[1]:
                                    array[i, k] = color_list[index]
                        else:
                            break
    return array


time_start = datetime.datetime.now()

list_random_colors = generale_color_list_gray("color_stadistics.csv")
print(len(list_random_colors))

base_matrix = create_matrix_color(10000, 6000, list_random_colors)
green_color_list = generale_color_list_green("color_stadistics.csv")  #Seleccionar los colores verdes
print("Cantidad de colores", len(green_color_list))
trees_matrix = make_trees(base_matrix, green_color_list, 50, 15)
trees_matrix = make_trees(trees_matrix, green_color_list, 80, 20)
trees_matrix = make_trees(trees_matrix, green_color_list, 100, 20)
trees_matrix = make_trees(trees_matrix, green_color_list, 125, 20)
trees_matrix = make_trees(trees_matrix, green_color_list, 140, 10)
trees_matrix = make_trees(trees_matrix, green_color_list, 160, 5)
trees_matrix = make_trees(trees_matrix, green_color_list, 175, 5)
trees_matrix = make_trees(trees_matrix, green_color_list, 200, 5)

# print(data2)
print("Dimensiones matriz", trees_matrix.shape)
img = Image.fromarray(trees_matrix)
img.save('big_artificial.png')
img = Image.fromarray(trees_matrix[:4000, :4000])  # A
img.save('big_artificialA.png')
img = Image.fromarray(trees_matrix[2000:6000, :4000])  # B
img.save('big_artificialB.png')
img = Image.fromarray(trees_matrix[:4000, 3000:7000])  # C
img.save('big_artificialC.png')
img = Image.fromarray(trees_matrix[2000:6000, 3000:7000])  # D
img.save('big_artificialD.png')
img = Image.fromarray(trees_matrix[:4000, 6000:])  # E
img.save('big_artificialE.png')
img = Image.fromarray(trees_matrix[2000:6000, 6000:])  # F
img.save('big_artificialF.png')
img = Image.fromarray(trees_matrix[1500:4500, 3000:6000])  # X
img.save('big_artificialX.png')

# img.show()

time_end = datetime.datetime.now()
diff = time_end - time_start

print("Segundos totales:", diff.seconds)