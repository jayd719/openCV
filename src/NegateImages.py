import cv2 as cv
import os

CACHE = "./cache/images/"

def save_image_to_disk(folder_name: str, filename: str, image) -> bool:
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        cv.imwrite(os.path.join(folder_name, filename), image)
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False

def process_image(file_path: str, file_name: str, function_name="random", process_fn=None) -> bool:
    try:
        img = cv.imread(os.path.join(file_path, file_name))
        if img is None:
            print(f"Invalid image: {file_name}")
            return False
        # Apply custom processing function if provided
        if process_fn:
            img_processed = process_fn(img)
        else:
            # Default: Invert the image
            img_processed = ~img
        return save_image_to_disk(os.path.join(CACHE, function_name), f"processed_{file_name}", img_processed)
    except Exception as e:
        print(f"Error processing image {file_name}: {e}")
        return False

# Example processing function
def invert_image(img):
    return ~img

# Main script
def main(src = "./assets/input_images/"):
    
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist.")
    else:
        for image in os.listdir(src):
            # Filter out non-image files
            if image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff',".tif")):
                process_image(src, image, function_name="invert", process_fn=invert_image)
                print(f"Processed: {image}")
            else:
                print(f"Skipped non-image file: {image}")

if __name__=="__main__":
    main()