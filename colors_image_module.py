class ColorBasic:
    def __init__(self, array):
        self.color = array  # rgb color matrix
        self.count = 1

    def increase_count(self):
        self.count +=1

    def increase_match(self, color):
        if self.color == color:
            self.count += 1


class ColorCounter:
    def __init__(self):
        self.color_list = list()
        self.color_index = list()

    def increase_color(self, color):
        for element in self.color_list:
            element.increase_match(color)

    def new_color(self, color):
        self.color_index.append(color)
        self.color_list.append(ColorBasic(color))

    def add_color(self, color):
        if color in self.color_index:
            self.increase_color(color)
        else:
            self.new_color(color)

    def populate_color_counter(self, matrix):
        count= 0
        print("pixels to processed", matrix.shape[0], "x", matrix.shape[1])
        for x in range(matrix.shape[0]):
            for y in range(matrix.shape[1]):
                new_color = matrix[x,y].tolist()
                self.add_color(new_color)
                if count % 10000 == 0:
                    print("processing pixel", count, new_color)
                count +=1

    def show_list_color(self):
        print(self.color_index)

    def show_len_list_color(self):
        print(len(self.color_index))

    def save_statistics_colors(self, path_destiny):
        f = open(path_destiny, "w+")
        for color in self.color_list:
            f.write(str(color.color) + " ; " + str(color.count) + "\n")
        f.close()

