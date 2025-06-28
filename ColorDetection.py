import cv2 as cv              # OpenCV for computer vision tasks
import numpy as np            # NumPy for numerical operations

# -------------------------------
# MASKING CONCEPT:
# Masking helps isolate specific regions in an image using binary masks.
# In a binary mask: white pixels (255) = regions of interest, black pixels (0) = ignored areas.
# -------------------------------

# === Initialize Webcam ===
cap = cv.VideoCapture(1)       # 0 selects the default camera

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Pre-define red color range in HSV space
lower_red = np.array([135, 85, 150], dtype=np.uint8)
upper_red = np.array([185, 250, 250], dtype=np.uint8)
kernel = np.ones((5, 5), dtype=np.uint8)  # Kernel for morphological operations

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read frame.")
        break

    # Flip frame horizontally to act like a mirror
    frame = cv.flip(frame, 1)

    # Convert BGR to HSV for better color filtering
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Create a binary mask where red colors are white
    red_mask = cv.inRange(hsv_frame, lower_red, upper_red)

    # Improve the mask using dilation (fill gaps in detected red regions)
    red_mask = cv.dilate(red_mask, kernel, iterations=1)

    # Extract only the red parts from the original frame
    red_highlighted = cv.bitwise_and(frame, frame, mask=red_mask)

    # Find contours from the mask
    contours, _ = cv.findContours(red_mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around sufficiently large red regions
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 300:
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv.putText(frame, "Red Color", (x, y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Show the processed frame
    cv.imshow("Detected Red Color", frame)

    # Break the loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv.destroyAllWindows()
