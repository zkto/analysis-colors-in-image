from scipy import misc
from colors_image_module import ColorCounter
import argparse

parser = argparse.ArgumentParser(description='Process to obtain colors from an image.')

parser.add_argument('--image-path', '--ip', dest='img_path',
                    required=True, metavar='PATH',
                    help='Path of the image')

parser.add_argument('--csv-path', '--cp', dest='csv_path',
                    required=True, metavar='PATH',
                    help='Path of the output_csv')

args = parser.parse_args()
print(args)
image_path = args.img_path
print(image_path)
csv_path = args.csv_path
print(csv_path)
arr_image = misc.imread(image_path)
list_colors = ColorCounter()
list_colors.populate_color_counter(arr_image)
# list_colors.show_list_color()
list_colors.show_len_list_color()
list_colors.save_statistics_colors(csv_path)
