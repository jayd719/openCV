
import cv2 as cv
import numpy
THRESHOLD = 123

def check_brightness(image):
    is_light = numpy.mean(image) > THRESHOLD

    return is_light

def addInvertedSection(image):
    imageInverted = ~image
    img3 = image.copy()
# replace values at coordinates (100, 100) to (399, 399) of img3 with region of img2
    img3[100:2400,100:2400,:] = imageInverted[100:2400,100:2400,:]
    return img3
    
# image = imread("hti.jpg")
image = cv.imread("hti.jpg")
image1 = cv.imread("image.png")


cv.imwrite("img_inv.png",addInvertedSection(image))
# cv.imwrite("img_inv1.png",addInvertedSection(image1))
print(check_brightness(image))

