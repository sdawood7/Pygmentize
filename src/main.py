import os
import argparse
import cv2 as cv
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument("--img_path", type=str)

flags = parser.parse_args()

def read_img(path):
    if not os.path.exists(path):
        print("Could not find given path. Please enter a valid path to the image.")
        return None

    with open(path, "r") as f:
        temp_img = cv.imread(path)
        img = np.asarray(temp_img)
        return img

print('Welcome to Pygmentize!')
bwImage = read_img(flags.img_path)
if bwImage.any():
    print("Success!")