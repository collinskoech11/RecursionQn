import matplotlib.pyplot as plt
from PIL import Image as image
import numpy as np
import math
import cv2

def open_image(filename):
    '''
    This function using the PIL library and numpy library to open an image file
    and create a black and white numpy array
    :param filename: The name of the file
    :return: a black and white version of the image in a numpy array with values of 0 and 1
    '''
    filename_name = str(input("PLease enter the filename : \n"))
    im = image.open(filename)#open the image file
    im_hsv = im.convert(mode='HSV') #change it to HSV
    np_hsv = np.ceil(np.array(im_hsv)/255) # scale to 0 to 1 and make binary
    return (np_hsv[:, :, 2]) #return the v channel which is black and white

def contains_pixel(im):
    '''
    This function uses the numpy.all() function to detect if a numpy array
    corresponding to a fractal image contains a non-white pixel
    :param im: a black and white image in a numpy array
    :return: False if the image is all non zero, True if at least one element is zero
    '''
    #doing this is faster than iterative becauses numpy
    if np.all(im): #np.all is True if all elements are not zero, if im contains a curve then np.all must be false
        return False #no curve detected
    else:
        return True #curve detected

def plot_line_fit(xt,yt):
    '''
    This function plots a scatter plot of xt vs yt and does a best fit line
    :param xt: x values to be plotted
    :param yt: y values to be plotted
    :return: the slope of the best fit line
    '''
    x = np.array(xt)
    y = np.array(yt)
    fit = np.polyfit(x,y,1)
    plt.scatter(x,y)
    plt.plot(x,fit[0]*x+fit[1])
    plt.show()
    return(fit[0])

def split_into_four(im, level, level_count):
    #students write your own doc string and comments


#This tells you the expected number of levels
#use this to initialize a list with zeros using a list comprehension
    num_level = (round(math.log2(float(im.shape[0])/4)))


filename = str(input("PLease enter the filename : \n"))

ImgData = [4 , 16 , 55 , 191 , 642 , 1981]
OtherImgData = [2 , 4 , 8 , 16 , 32 , 64] 
plt.plot(Year, Population)
plt.title(' ')
plt.xlabel(' ')
plt.ylabel(' ')
plt.show()


print("1. 78 67 263 828664404")
