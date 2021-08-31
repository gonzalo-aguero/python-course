import cv2 as cv
import numpy as np
noises = cv.CascadeClassifier('/home/gonzalo90fa/Desktop/Development projects/Curso Python 1/facialRecognition/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
camera = cv.VideoCapture(0)

while True:
    _,capture = camera.read()
    grays = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)
    face = noises.detectMultiScale(grays, 1.9, 8)
    for(x, y, v1, v2) in face:
        cv.rectangle(capture, (x, y), (x+v1, y+v2), (150,0,200), 2)
    cv.imshow("Result", capture) 

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()