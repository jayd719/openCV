import os
from src.ProcessResultsHTML import process_results
from src.functions import*
from src.ImageProcessor.ProcessImage import process_image,CACHE
from setup import *



# Main script
def process_folder(src = "./assets/input_images/"):
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist.")
    else:
        for image in os.listdir(src):
            # Filter out non-image files
            if image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff',".tif")):
                process_image(src, image, function_name="invert", process_fn=invert_image,save_as_jpep=True)
                process_image(src, image, function_name="Original", process_fn=convert_to_jpg,save_as_jpep=True)
                process_image(src,image,function_name="darken",process_fn=brithen,save_as_jpep=True)
                process_image(src,image,function_name="darken1",process_fn=brithen,save_as_jpep=True)
                process_image(src,image,function_name="darken2",process_fn=brithen,save_as_jpep=True)
                
                print(f"Processed: {image}")
            else:
                print(f"Skipped non-image file: {image}")

if __name__=="__main__":
    
    process_folder(PATH)
    process_results(CACHE,f"cache/")