"""-------------------------------------------------------
Computer Vision: Process Image
-------------------------------------------------------
Author:  JD
ID:      91786
Project: OpenCV
Version:  1.0.8
__updated__ = Thu Dec 19 2024
-------------------------------------------------------
"""

import cv2 as cv
import os
from setup import CACHE


def save_image_to_disk(folder_name: str, filename: str, image, convertToJPG=False) -> bool:
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            
        if convertToJPG:
            filename = filename.split(".")[0]
            filename = f"{filename}.jpg"
        cv.imwrite(os.path.join(folder_name, filename), image)
        return os.path.join(folder_name, filename)
    except Exception as e:
        print(f"Error saving image: {e}")
        return False


def process_image(file_path: str, file_name: str, function_name="random", process_fn=None, save_as_jpep=False) -> bool:
    try:
        img = cv.imread(os.path.join(file_path,file_name))
        if img is None:
            print(f"Invalid image: {file_name}")
            return False
        # Apply custom processing function if provided
        if process_fn:
            img_processed = process_fn(img)
        else:
            # Default: Invert the image
            img_processed = ~img
        return save_image_to_disk(os.path.join(CACHE, function_name), f"{function_name}_{file_name}", img_processed, save_as_jpep)
    except Exception as e:
        print(f"Error processing image {file_name}: {e}")
        return False

def process_image_func(imageObject ,function_name="random", process_fn=None, save_as_jpep=False) -> bool:

    try:
        if imageObject.image is None:
            print(f"Invalid image: {imageObject.name}")
            return False
        # Apply custom processing function if provided
        if process_fn:
            img_processed = process_fn(imageObject.image)
        else:
            # Default: Invert the image
            
            img_processed = ~imageObject.image
        imageObject.history.update({function_name:save_image_to_disk(os.path.join(CACHE, function_name), f"{function_name}_{imageObject.name}", img_processed, save_as_jpep)})
        return img_processed
    except Exception as e:
        print(f"Error processing image {imageObject.name}: {e}")
        return None