import os
from src.Uti.ProcessResultsHTML import process_results
from src.ImageProcessors.functions import invert_image, convert_to_jpg, brighten_image  
from src.ImageProcessors.ProcessImage import process_image
from src.Drawing.writeTextToImage import write_text
from setup import PATH,CACHE
# Main script
def test_directory(src="./assets/input_images/"):
    """Process images in a folder and apply transformations."""
    if not os.path.exists(src):
        print(f"Source directory '{src}' does not exist.")
        return

    os.makedirs(CACHE, exist_ok=True)

    for image in os.listdir(src):
        # Filter out non-image files
        if image.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.tif')):
            try:
                
                # Apply multiple transformations
                transformations = {
                    # "invert": invert_image,
                    "original": convert_to_jpg,
                    # "Brighten 10": lambda img: brighten_image(img, 10),
                    # "Darken  100": lambda img: brighten_image(img, -100),
                    "Brighten 30": lambda img: write_text(img),
                }

                for function_name, process_fn in transformations.items():
                    process_image(
                        src, image, function_name=function_name, process_fn=process_fn, save_as_jpep=True
                    )
                
                print(f"Processed: {image}")
            except Exception as e:
                print(f"Error processing {image}: {e}")
        else:
            print(f"Skipped non-image file: {image}")

if __name__ == "__main__":
    try:
        # Process input folder
        test_directory(PATH)
        # Generate HTML results
        process_results(CACHE, output_dir="cache", output_file="results.html")
    except Exception as e:
        print(f"An error occurred: {e}")
