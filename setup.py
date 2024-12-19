import os
from src.ProcessResultsHTML import process_results
from src.functions import*
from src.ProcessImage import process_image,CACHE


# Main script
def main(src = "./assets/input_images/"):
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist.")
    else:
        for image in os.listdir(src):
            # Filter out non-image files
            if image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff',".tif")):
                process_image(src, image, function_name="invert", process_fn=invert_image,save_as_jpep=True)
                process_image(src, image, function_name="Original", process_fn=convert_to_jpg,save_as_jpep=True)
                print(f"Processed: {image}")
            else:
                print(f"Skipped non-image file: {image}")

if __name__=="__main__":
    PATH ="./assets/input_images/"
    main(PATH)
    process_results(CACHE,"out/")