import cv2 as cv

# FUNCTION ON IMAGE
def invert_image(img):
    return ~img

def convert_to_jpg(img):
    return img

def brighten_image(img,value):
    return cv.convertScaleAbs(img, alpha=1, beta=value)