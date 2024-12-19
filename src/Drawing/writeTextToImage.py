import cv2 as cv
import math

def write_text(img, position=(None, None), text="Sample Text"):

    img = cv.resize(img, (512, 512), cv.INTER_LINEAR)
    h, w, _ = img.shape

    print(f"Image dimensions: Height={h}, Width={w}")

    thickness = 10
    color_green = (0, 255, 0)
    color_red = (255, 0, 0)
    color_blue = (0, 0, 255)

    cv.line(img, (0, 0), (w - 1, h - 1), color_green, thickness)
    cv.line(img, (w - 1, 0), (0, h - 1), color_green, thickness)

    margin = 10
    step = h // 10

    left, right = margin, w - margin
    top, bottom = margin, h - margin


    while left < right and top < bottom:
        cv.rectangle(img, (left, top), (right, bottom), color_red, thickness)
        left += step
        right -= step
        top += step
        bottom -= step

    center_x, center_y = w // 2, h // 2
    radius = 10

    while radius < center_x and radius < center_y:
        cv.circle(img, (center_x, center_y), radius, color_blue, thickness)
        radius += step


    font = cv.FONT_HERSHEY_SIMPLEX
    text_position = (center_x - 200, center_y) 
    cv.putText(img, text, text_position, font, 3, color_green, thickness, cv.LINE_AA)

    return img
