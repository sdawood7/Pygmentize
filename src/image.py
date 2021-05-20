import os
import datetime
import dateutil.tz
import cv2 as cv
import numpy as np

#class to encapsulate functions for images
class Image:
    #this function checks to see if the path was valid and also reads the image :D
    @staticmethod
    def read_img_file(path):
        if not os.path.exists(path):
            print("Could not find given path. Please enter a valid path to the image.")
            return np.array(0)

        temp_img = cv.imread(path)
        img = np.asarray(temp_img) #convert img numpy array :D
        return img

    @staticmethod
    def read_imgs(path):
        img_list = list()
        if not os.path.exists(path):
            print("Could not find given path. Please enter a valid path to the image.")
            return img_list

        if os.path.isdir(path):
            for filename in os.listdir(path):
                img_list.append(Image.read_img_file(os.path.join(path, filename)))
            return img_list

        if os.path.isfile(path):
            img_list.append(Image.read_img_file(path))
            return img_list

        return img_list

    #write numpy img to output file
    @staticmethod
    def write_img(path, img):
        if path is None:
            print("No output path given. Please enter a valid path to the image.")
            return

        if not os.path.exists(path):
            os.makedirs(path)

        now = datetime.datetime.now(dateutil.tz.tzlocal())
        timestamp = now.strftime("%Y_%m_%d_%H_%M_%S") #Use the current time to ensure a file is created without conflicts.

        img_path ="{}{}.png".format(path, timestamp)
        with open(img_path, "w") as f:
            cv.imwrite(img_path, img) #Write image to given path
            return
    
    @staticmethod
    def img_to_bw(img, ratios):
        def pixel_to_bw(pixel_val):
            blue, green, red = pixel_val[0], pixel_val[1], pixel_val[2]
            return ((ratios['blue'] * blue), (ratios['green'] * green), (ratios['red'] * red)) #Return the sum of the ratios of each pixel value

        gray_img = np.ndarray([img.shape[0], img.shape[1], 3], dtype=int) #Create an array with the same height and width as the input image, and 1 channel for grayscale value
        for i in range(gray_img.shape[0]): #Loop through the pixels in the width of the image
            for j in range(gray_img.shape[1]): #Loop through the pixels in the height of the image
                gray_img[i][j] = pixel_to_bw(img[i][j]) 
        return gray_img

    @staticmethod
    def img_to_col(img, ratios):
        def pixel_to_col(pixel_val):
            blue = int(pixel_val * ratios['blue']) #Calculate the blue value based on the given ratio
            green = int(pixel_val * ratios['green']) #Calculate the green value based on the given ratio
            red = int(pixel_val * ratios['red']) #Calculate the red value based on the given ratio
            return (blue, green, red) #Return the values in B,G,R order

        color_img = np.ndarray([img.shape[0], img.shape[1], 3], dtype=int) #Create an array with the same height and width as the input image, and 3 channels for red, blue, green values
        for i in range(color_img.shape[0]): #Loop through the pixels in the width of the image
            for j in range(color_img.shape[1]): #Loop through the pixels in the height of the image
                cur_pixel = int((int(img[i][j][0]) + int(img[i][j][1]) + int(img[i][j][2])) / 3) # Average the blue green and red values from the input image
                color_img[i][j] = pixel_to_col(cur_pixel)
        return color_img
