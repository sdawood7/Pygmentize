import os
import argparse
import cv2 as cv
import numpy as np

#this object is used to parse command line arguments :D
parser = argparse.ArgumentParser()
#this is an argument for the directory of an img
parser.add_argument("--img_path", type=str)
#this stores the values of the parsed command line arguments
flags = parser.parse_args()

#this function checks to see if the path was valid and also reads the image :D
def read_img(path):
    if not os.path.exists(path):
        print("Could not find given path. Please enter a valid path to the image.")
        return None

    with open(path, "r") as f:
        temp_img = cv.imread(path)
        img = np.asarray(temp_img) #convert img numpy array :D
        return img

print('Welcome to Pygmentize!')
bwImage = read_img(flags.img_path)
if bwImage.any(): #verify img is in numpy array
    print("Success!")

