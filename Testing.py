"""-------------------------------------------------------
Computer Vision: Module Description Here
-------------------------------------------------------
Author:  JD
ID:      91786
Project: OpenCV
Version:  1.0.8
__updated__ = Thu Dec 19 2024
-------------------------------------------------------
"""

import shutil
import cv2 as cv
from src.ImageProcessors.functions import *
from src.Uti.ProcessResultsHTML import process_results
from setup import CACHE,PATH
from src.ImageProcessors.writeTextToImage import write_text
from src.Uti.ProcessDir import process_directory
from src.ImageProcessors.thresholding import *
from src.ImageProcessors.this import ImageOI

transformations = {
    "1ORIGINAL": convert_to_jpg,
    # "Marked": lambda img: write_text(img),
    # "Gaussian":lambda img:apply_guassian_blur(img,5,3)
    "THRESH_BINARY_INV": thresh_binary_inv,
    "THRESH_TRUNC": thresh_trunc,
    "THRESH_TOZERO": thresh_tozero,
    "THRESH_TOZERO_INV": thresh_tozero_inv
}

if __name__ == "__main__":
    shutil.rmtree(CACHE)
    process_directory()    
    process_results(CACHE, "cache/")
    
