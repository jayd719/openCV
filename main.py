import numpy as np
import shutil
from src.ImageProcessors.ProcessImage import save_image_to_disk
from src.Uti.ProcessResultsHTML import process_results
from setup import CACHE
from src.Drawing.writeTextToImage import write_text
from src.Uti.ProcessDir import test_directory



if __name__ =="__main__":
    
    test_directory()
    process_results(CACHE,"cache/")