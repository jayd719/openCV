"""-------------------------------------------------------
Computer Vision: Testing
-------------------------------------------------------
Author:  JD
ID:      91786
Project: OpenCV
Version:  1.0.8
__updated__ = Thu Dec 19 2024
-------------------------------------------------------
"""


from src.ImageProcessors.functions import *
from src.Uti.ProcessResultsHTML import process_results
from src.ImageProcessors.writeTextToImage import write_text
from src.Uti.ProcessDir import process_directory
from src.ImageProcessors.ProcessImage import process_image_func
from src.ImageProcessors.thresholding import *
from src.ImageProcessors.ImageIO import ImageOI
from src.Uti.app import app
from setup import CACHE,PATH
import shutil
import cv2 as cv

transformations = {
    "original": convert_to_jpg,
    "Marked": lambda img: write_text(img),
    "Gaussian":lambda img:apply_guassian_blur(img,5,3),
    "THRESH_BINARY_INV": thresh_binary_inv,
    "THRESH_TRUNC": thresh_trunc,
    "THRESH_TOZERO": thresh_tozero,
    "THRESH_TOZERO_INV": thresh_tozero_inv
}

if __name__ == "__main__":
    shutil.rmtree(CACHE)

    for image in os.listdir(PATH):
        source_image = ImageOI(image,os.path.join(PATH,image))
        source_image.resize()

        process_image_func(source_image,"INVERT",invert_image,True)
        process_image_func(source_image,"BRIGHTN",lambda img: brighten_image(img, 10),True)
        process_image_func(imageObject=source_image,function_name="HTRE",process_fn=thresh_tozero_inv,save_as_jpep=True)
        source_image.save()
        print(image)
    
    process_results(CACHE, "cache/")
    # app.run(debug=True)
    
