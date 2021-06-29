# import argparse
import cgi
from image import Image

#this object is used to parse command line arguments :D
# parser = argparse.ArgumentParser()
#this is an argument for the directory of an img
# parser.add_argument("--img_path", type=str, help="The path to the input image.")
# parser.add_argument("--out_path", type=str, default=".\out_dir\\", help="The directory path to output new images to.")
#this stores the values of the parsed command line arguments
# flags = parser.parse_args()

#constants for converting from color to bw
#ratios in range from 0.0 <= x <= 1.0
ratios_to_bw = {'red' : 1.0, 'blue' : 1.0, 'green' : 1.0}

#constants for converting from bw to color
#ratios in range from 0.0 <= x <= 1.0
ratios_to_col = {'red' : 1.0, 'blue' : 0.0, 'green' : 1.0}

def main(img_path):
    print('Welcome to Pygmentize!')
    img_list = Image.read_imgs(img_path) #List for multiple images!
    for img in img_list:
        if img.any(): #check if any images were read
            new_img = Image.img_to_col(img, ratios_to_col)
            # Image.write_img(, new_img)
    print("Success!")

form = cgi.FieldStorage()
img_path = form.getvalue('img_path')
main(img_path)