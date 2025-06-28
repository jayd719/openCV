import cv2 as cv  # OpenCV library for computer vision tasks
import numpy as np  # NumPy for array manipulations


# === Image Setup ===

# Create a blank image of size 800x800 pixels, with 3 color channels (BGR)
# dtype=np.uint8 ensures pixel values range from 0–255
img = np.zeros((800, 800, 3), dtype=np.uint8)

# Fill entire image with green (BGR format: Blue=0, Green=255, Red=0)
img[:] = 0, 255, 0

# Color a specific rectangular region red (rows 200–300, columns 300–400)
img[200:300, 300:400] = 0, 0, 255

# === Drawing Shapes ===

# Draw a red rectangle from (40,40) to (100,100) with line thickness 2 pixels
cv.rectangle(img, (40, 40), (100, 100), (0, 0, 255), thickness=2)

# Draw another rectangle with the same color and thickness
cv.rectangle(img, (140, 140), (200, 200), (0, 0, 255), thickness=2)

# Draw a red circle centered at (500,500) with radius 100 and thickness 10
cv.circle(img, (500, 500), 100, (0, 0, 255), thickness=10)

# Draw two diagonal red lines forming an 'X' across the image
cv.line(img, (0, 0), (800, 800), (0, 0, 255), 2)
cv.line(img, (800, 0), (0, 800), (0, 0, 255), 2)

# === Adding Text ===

# Put red text "this is new text" at position (200,700)
# Using Hershey Triplex font, font scale 1, and thickness 1
cv.putText(img, "this is new text", (200, 700), cv.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1)

# === Displaying Image ===

cv.imshow("test Image", img)  # Open a window showing the image
cv.waitKey(0)  # Wait for any key press
cv.destroyAllWindows()  # Close all OpenCV windows
