"""-------------------------------------------------------
Computer Vision: Module Description Here
-------------------------------------------------------
Author:  JD
ID:      91786
Project: OpenCV
Version:  1.0.8
__updated__ = Sat Dec 21 2024
-------------------------------------------------------
"""

import cv2 as cv
import numpy as np
from src.ImageProcessors.ProcessImage import save_image_to_disk
from setup import DEBUG, CACHE

DETECTOR = cv.SIFT_create()

class ImageOI:

    def __init__(self, name, image_path):
        self.name = name
        self.image = cv.imread(image_path)
        
        if self.image is None:
            return None
        self.path = image_path
        self.latest= self.image
        self.history ={}
    
    def resize(self,h=512):
        self.image = cv.resize(self.image,(h,h))
        self.latest = cv.resize(self.latest,(h,h))

    def save(self, path=f"{CACHE}"):
        save_image_to_disk(f"{path}/1ORIGINAL", self.name, self.image, True)
        for function,image in self.history.items():
            print(f"\t{function} : {image}")

