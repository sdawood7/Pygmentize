import os
import argparse
import datetime
import dateutil.tz
import cv2 as cv
import numpy as np

#constants for converting from color to bw
#ratios MUST add to 1.0
red_c2b_ratio = 0.3333
blue_c2b_ratio = 0.3333
green_c2b_ratio = 0.3334

#constants for converting from bw to color
#sum of ratios must be <= 3.0
red_b2c_ratio = 1
blue_b2c_ratio = 0
green_b2c_ratio = 1

#this object is used to parse command line arguments :D
parser = argparse.ArgumentParser()
#this is an argument for the directory of an img
parser.add_argument("--img_path", type=str, help="The path to the input image.")
parser.add_argument("--out_path", type=str, default=".\out_dir\\", help="The directory path to output new images to.")
#this stores the values of the parsed command line arguments
flags = parser.parse_args()

#this function checks to see if the path was valid and also reads the image :D
def read_img(path):
    if not os.path.exists(path):
        print("Could not find given path. Please enter a valid path to the image.")
        return np.array(0)

    temp_img = cv.imread(path)
    img = np.asarray(temp_img) #convert img numpy array :D
    return img

#write numpy img to output file
def write_img(path, img):
    if path is None:
        print("No output path given. Please enter a valid path to the image.")
        return

    if not os.path.exists(path):
        os.makedirs(path)

    now = datetime.datetime.now(dateutil.tz.tzlocal())
    timestamp = now.strftime("%Y_%m_%d_%H_%M_%S")

    img_path ="{}{}.png".format(path, timestamp)
    with open(img_path, "w") as f:
        cv.imwrite(img_path, img)
        return

def img_to_bw(img):
    def pixel_to_bw(pixel_val):
        blue, green, red = pixel_val[0], pixel_val[1], pixel_val[2]
        return int((blue_c2b_ratio * blue) + (green_c2b_ratio * green) + (red_c2b_ratio * red))

    gray_img = np.ndarray([img.shape[0], img.shape[1]], dtype=int)
    for i in range(gray_img.shape[0]):
        for j in range(gray_img.shape[1]):
            gray_img[i][j] = pixel_to_bw(img[i][j])
    return gray_img

def img_to_col(img):
    def pixel_to_col(pixel_val):
        blue = int(pixel_val * blue_b2c_ratio)
        green = int(pixel_val * green_b2c_ratio)
        red = int(pixel_val * red_b2c_ratio)
        return (blue, green, red)

    color_img = np.ndarray([img.shape[0], img.shape[1], 3], dtype=int)
    for i in range(color_img.shape[0]):
        for j in range(color_img.shape[1]):
            cur_pixel = int((int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2])) / 3)
            color_img[i][j] = pixel_to_col(cur_pixel)
    return color_img

def main():
    print('Welcome to Pygmentize!')
    bwImage = read_img(flags.img_path)
    if bwImage.any(): #verify img is in numpy array
        new_img = img_to_col(bwImage)
        write_img(flags.out_path, new_img)
        print("Success!")

if __name__ == '__main__':
    main()