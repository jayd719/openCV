import cv2 as cv
import numpy as np


webcam = cv.VideoCapture(1)

face_cascade = cv.CascadeClassifier(r"haarcascade_frontalface_default.xml")

while webcam.isOpened():
    ret, frame = webcam.read()
    frame = cv.flip(frame, 1)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10)

    for x, y, w, h in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv.putText(
        frame,
        f"Faces: {len(faces)}",
        (10, 30),
        cv.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )
    cv.imshow("Output", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break


webcam.release()
cv.destroyAllWindows()
