import cv2 as cv
import numpy as np
import time


def nothing(x): pass

# === Create Trackbars for HSV Threshold Tuning ===
cv.namedWindow("Trackbars")
cv.createTrackbar("LH", "Trackbars", 0, 180, nothing)
cv.createTrackbar("LS", "Trackbars", 120, 255, nothing)
cv.createTrackbar("LV", "Trackbars", 70, 255, nothing)
cv.createTrackbar("UH", "Trackbars", 10, 180, nothing)
cv.createTrackbar("US", "Trackbars", 255, 255, nothing)
cv.createTrackbar("UV", "Trackbars", 255, 255, nothing)

# Color detection mode
color_mode = 'red'

# Morphological kernel
kernel = np.ones((5, 5), np.uint8)

# Start webcam
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

# Time for FPS tracking
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    frame = cv.resize(frame, (640, 480))
    frame = cv.flip(frame, 1)
    blurred = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(blurred, cv.COLOR_BGR2HSV)

    # Get HSV thresholds from trackbars
    lh = cv.getTrackbarPos("LH", "Trackbars")
    ls = cv.getTrackbarPos("LS", "Trackbars")
    lv = cv.getTrackbarPos("LV", "Trackbars")
    uh = cv.getTrackbarPos("UH", "Trackbars")
    us = cv.getTrackbarPos("US", "Trackbars")
    uv = cv.getTrackbarPos("UV", "Trackbars")

    lower = np.array([lh, ls, lv], dtype=np.uint8)
    upper = np.array([uh, us, uv], dtype=np.uint8)

    # Apply color masks based on selected mode
    if color_mode == 'red':
        lower_red1 = np.array([0, 120, 70], np.uint8)
        upper_red1 = np.array([10, 255, 255], np.uint8)
        lower_red2 = np.array([170, 120, 70], np.uint8)
        upper_red2 = np.array([180, 255, 255], np.uint8)
        mask1 = cv.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv.inRange(hsv, lower_red2, upper_red2)
        mask = cv.bitwise_or(mask1, mask2)
    else:
        mask = cv.inRange(hsv, lower, upper)

    # Morphological operations
    mask = cv.dilate(mask, kernel, iterations=1)

    # Find contours
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 300:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            label = f"{color_mode.capitalize()} Color"
            cv.putText(frame, label, (x, y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # === FPS Calculation ===
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    cv.putText(frame, f"FPS: {fps:.2f}", (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the results
    cv.imshow("Detected Color", frame)
    cv.imshow("Mask", mask)

    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv.imwrite("screenshot.png", frame)
        print("Saved screenshot.")
    elif key == ord('r'):
        color_mode = 'red'
        print("Switched to red detection mode.")
    elif key == ord('g'):
        color_mode = 'green'
        print("Switched to green detection mode.")
    elif key == ord('b'):
        color_mode = 'blue'
        print("Switched to blue detection mode.")

# Cleanup
cap.release()
cv.destroyAllWindows()
