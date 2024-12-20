

import os
import cv2 as cv
from src.Uti.ProcessResultsHTML import process_results
from src.ImageProcessors.ProcessImage import process_image
from src.ImageProcessors.writeTextToImage import write_text
from src.ImageProcessors.functions import invert_image, convert_to_jpg, brighten_image, preprocess
from src.ImageProcessors.thresholding import *
from setup import PATH, CACHE

# Apply multiple transformations
transformations = {
    "invert": invert_image,
    "1original": convert_to_jpg,
    "Brighten 10": lambda img: brighten_image(img, 10),
    "Darken  100": lambda img: brighten_image(img, -100),
    "Marked": lambda img: write_text(img),
    "Prep": lambda img: preprocess (img),
    "THRESH_BINARY_INV": thresh_binary_inv,
    "THRESH_TRUNC": thresh_trunc,
    "THRESH_TOZERO": thresh_tozero,
    "THRESH_TOZERO_INV": thresh_tozero_inv
}


# Main script
def process_directory(src="./assets/input_images/", transformations=transformations, limit=None):
    """Process images in a folder and apply transformations."""
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist.")
        return

    os.makedirs(CACHE, exist_ok=True)

    for image in os.listdir(src):
        # Filter out non-image files
        if image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif')):
            try:
                for function_name, process_fn in transformations.items():
                    e1 = cv.getTickCount()
                    process_image(src, image, function_name=function_name, process_fn=process_fn, save_as_jpep=True)
                    e2 = cv.getTickCount()
                    time = (e2-e1)/cv.getTickFrequency()
                    print(f"Image:[{image}] Process In: [{time:.4f}]")
                    
                print(f"Processed: {image}")
            except Exception as e:
                print(f"Error processing {image}: {e}")
        else:
            print(f"Skipped non-image file: {image}")


if __name__ == "__main__":
    try:
        # Process input folder
        process_directory(PATH)
        # Generate HTML results
        process_results(CACHE, output_dir="cache", output_file="results.html")
    except Exception as e:
        print(f"An error occurred: {e}")
