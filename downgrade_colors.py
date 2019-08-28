from scipy import misc
from PIL import Image
import argparse
from downgrade_colors_module import downgrade_colors

parser = argparse.ArgumentParser(description='Process to downgrade colors from an image')

parser.add_argument('--paths', '--p', dest='paths', nargs=2,
                    required=True, metavar='PATH',
                    help='Paths of the image files (origin and destiny)')

args = parser.parse_args()
input_img = args.paths[0]
output_img = args.paths[1]

arr_image = misc.imread(input_img)
arr_image_new = downgrade_colors(arr_image)

img = Image.fromarray(arr_image_new)
img.save(output_img)
print("Image succesfully downgrade !")

