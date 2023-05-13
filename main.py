import cv2 as cv
import os

cam = "https://api.ucsb.edu/dining/cams/v2/stream/carrillo?ucsb-api-key=0AVpBy0HfloWaEQHPanHTGSYmXusaNIJ"


cap = cv.VideoCapture(cam)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()