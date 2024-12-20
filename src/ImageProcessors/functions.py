"""-------------------------------------------------------
Computer Vision: Custom Functions Lib
-------------------------------------------------------
Author:  JD
ID:      91786
Project: OpenCV
Version:  1.0.8
__updated__ = Thu Dec 19 2024
-------------------------------------------------------
"""

import cv2 as cv


# FUNCTION ON IMAGE
def invert_image(img):
    return ~img


def convert_to_jpg(img):
    return img


def brighten_image(img, value):
    return cv.convertScaleAbs(img, alpha=1, beta=value)


def preprocess(img, h=512):
    cv.resize(img, (h, h), interpolation=cv.INTER_CUBIC)
    return img


def apply_guassian_blur(img,kernelSize=3, sigma=1):
    img = cv.GaussianBlur(img,(kernelSize,kernelSize),sigma)
    return img