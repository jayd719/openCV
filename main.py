import cv2 as cv
import numpy as np
import shutil
from src.ImageProcessors.ProcessImage import save_image_to_disk
from src.Uti.ProcessResultsHTML import process_results
from setup import CACHE
from src.Drawing.writeTextToImage import write_text
from src.Uti.ProcessDir import test_directory



if __name__ =="__main__":
    shutil.rmtree(CACHE)
    img=np.zeros((512,512,3),np.uint8)
    img = write_text(img)
    save_image_to_disk(f"{CACHE}/drawing","one",img,True)
    
    
    # test_directory()
    process_results(CACHE,"cache/")