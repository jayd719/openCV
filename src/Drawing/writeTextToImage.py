import cv2 as cv

def write_text(img,position=(None,None),text="Sample Text"):
    h,w,s =img.shape
    print(f"{h} {w}")
    thick = 10
    color = (0,255,0)
    cv.line(img,(0,0),(h-1,w-1),color,thick)
    cv.line(img,(h-1,0),(0,w-1),color,thick)
    
    
    return img