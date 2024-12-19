import cv2 as cv

# FUNCTION ON IMAGE
def invert_image(img):
    return ~img

def convert_to_jpg(img):
    return img

def brighten_image(img,value):
    return cv.convertScaleAbs(img, alpha=1, beta=value)

def preprocess(img,h=512):
    cv.resize(img,(h,h),interpolation=cv.INTER_CUBIC)
    return img