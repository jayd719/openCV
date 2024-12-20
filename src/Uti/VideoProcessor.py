import cv2 as cv

cap = cv.VideoCapture("./assets/input_videos/video.mp4")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    cv.imshow("frame", frame)
    
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
