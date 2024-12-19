# Project Overview
This project provides a beginner-friendly toolkit for image processing with OpenCV, designed to simplify the process of experimenting with image transformations. It abstracts away tedious tasks such as loading, saving, and correctly rendering images, allowing users to focus on creating and applying transformations. Processed results are displayed directly on a live webpage, enabling real-time visualization of changes without the need to switch between tools, folders, or interfaces


## Key Features:
- <b>Live Server Integration:</b>Run the toolkit using a live server, where all changes are instantly reflected in the browser.
- <b>Real-Time Results:</b> Create Python functions that take input images, apply transformations, and return the modified 
images. Changes are displayed dynamically without navigating between directories using a CLI or GUI file explorer.


## Functions

### ImageProcessor
The process_image function is the core utility for applying custom image processing functions to an input image. It simplifies the workflow by handling file management, processing, and optional output customization.

<pre>
from src.ImageProcessor.ProcessImage import process_image

def process_image(file_path: str, file_name: str, function_name="random", process_fn=None, save_as_jpeg=False) -> bool:
</pre>

- <b>file_path (str):</b> The directory path where the 
input image is located.
    -  Example: "./assets/input_images/".
- <b>file_name (str):</b> The name of the input image file (including the extension).
    - Example: "example.png"
- <b>function_name (str):</b> Name of the function, which specifies the folder where the output images will be saved. By default, the folder is named 'random'.
    - Default: "random"
    -  Example: "invert"

- <b>process_fn (callable):</b> A Python function that defines the image processing logic.The function should accept an input image and return the processed image.
    - Example: <pre>
                    def invert_colors(image):
                        return cv2.bitwise_not(image)
                </pre>

- <b>save_as_jpeg (bool):</b> Save output as JPG instead of origin format



<hr>

### ProcessResultsHTML

The process_results function is a utility for consolidating processed images and displaying them in an organized HTML file. It takes the processed image files from a source directory, generates an HTML report, and saves the report to the specified output directory.
<pre>
from src.ProcessResultsHTML import process_results

def process_results(src="src", output_dir="out", output_file="results.html"):
</pre>

- <b>src (str):</b> The source directory where processed images are stored.
    - Example: If your processed images are in ./cache/images/, set src="cache/images"

- <b>output_dir (str):</b> The directory where the resulting HTML file will be saved.
    - Example: "./reports/"
- <b>output_file (str):</b> The name of the HTML file to generate.
    - Example: "processed_images_report.html"


<img src ="plugins/results2.png" width="50%">


## Project Structure
<pre>
PROJECT/
│
├── .devcontainer/           # DevContainer configuration for remote or containerized development
├── .env                     # Environment variables for the project
├── .github/                 # GitHub-specific workflows and configurations
├── assets/                  # Input media files (images and videos)
│   └── input_images/        # Add input images or videos here
│
├── cache/                   # Stores processed images (output files)
│   └── images/              # Automatically generated processed images
│
├── ideas/                   # Placeholder for project-related ideas or future plans
├── js/                      # JavaScript files (if applicable for the frontend)
├── log/                     # Logs generated during runtime
├── out/                     # Contains final output files (like reports or results)
│   └── results.html         # Auto-generated HTML file showing processed results
│
├── plugins/                 # Plugins or helper assets (e.g., images, external scripts)
│   └── results.png          # Example image used in the documentation
│
├── src/                     # Source code directory
│   ├── ImageProcessor/      # Core image processing functionality
│   │   ├── __init__.py      # Package initialization
│   │   └── functions.py     # Main functions for processing images
│   └── ProcessResultsHTML.py # Generates HTML reports for processed images
│
├── templates/               # HTML or Jinja templates (if applicable)
├── testsuml/                # Testing utilities or scripts
├── uml/                     # UML diagrams or architecture documentation
│
├── .editorconfig            # Editor configuration for consistent coding styles
├── .gitignore               # Specifies files and directories ignored by Git
├── .gitpod.Dockerfile       # Dockerfile for Gitpod development environment
├── .gitpod.yml              # Gitpod configuration file
├── .prettierrc              # Configuration for Prettier code formatting
├── CONTRIBUTING.md          # Guidelines for contributing to the project
├── LICENSE.txt              # License information
├── main.py                  # Main entry point for the application
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
├── SECURITY.md              # Security guidelines
├── setup.py                 # Python package setup

</pre>


The structure includes directories for input files (assets/input_images/), processed outputs (cache/images/), and reports (out/results.html). Core logic resides in src/, featuring modules for image processing (ImageProcessor/functions.py) and HTML report generation (ProcessResultsHTML.py). Configurations like .editorconfig ensure consistent coding styles, while .gitpod.Dockerfile and .gitpod.yml enable streamlined containerized development. The project also includes detailed documentation (README.md, CONTRIBUTING.md) and excludes temporary files using .gitignore.