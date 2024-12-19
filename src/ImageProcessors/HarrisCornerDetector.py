import cv2 as cv
import numpy as np

def harris_corner_detector(img):
    gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray = np.float32(gray_img)
    dst = cv.cornerHarris(gray_img,2,3,0.04)
    dst = cv.dilate(dst,None)
    return img