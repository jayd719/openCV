import cv2 as cv
import numpy as np
import os 
from src.ImageProcessors.ProcessImage import save_image_to_disk

def thresh_binary_inv(img, threshold=127):
    cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return cv.threshold(img, threshold, 255, cv.THRESH_BINARY_INV)[1]

def thresh_trunc(img, threshold=120):
    cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return cv.threshold(img, threshold, 255, cv.THRESH_TRUNC)[1]

def thresh_tozero(img, threshold=200):
    cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return cv.threshold(img, threshold, 255, cv.THRESH_TOZERO)[1]

def thresh_tozero_inv(img, threshold=10):
    cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    return cv.threshold(img, threshold, 255, cv.THRESH_TOZERO_INV)[1]



