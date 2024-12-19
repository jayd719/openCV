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
from src.ImageProcessors.functions import convert_to_jpg
from src.Uti.ProcessResultsHTML import process_results
from setup import CACHE
from src.ImageProcessors.writeTextToImage import write_text
from src.Uti.ProcessDir import process_directory

transformations = {
    "original": convert_to_jpg,
    "Marked": lambda img: write_text(img)
}

if __name__ == "__main__":
    shutil.rmtree(CACHE)
    process_directory(transformations=transformations)
    process_results(CACHE, "cache/")
    
