import cv2 as cv
import os

model = 'Gonzalo'
path1 = './data'
fullpath = path1 + '/' + model
if not os.path.exists(fullpath):
    os.makedirs(fullpath)

# Elements that are not faces
noises = cv.CascadeClassifier('/home/gonzalo90fa/Desktop/Development projects/Curso Python 1/facialRecognition/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
camera = cv.VideoCapture(0)
color = (150,0,200)

imageId = 1
while True:
    response,capture = camera.read()
    if response == False: break

    grays = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)#Conver image to grays scale
    captureId = capture.copy()
    face = noises.detectMultiScale(grays, 1.3, 10)#Detect faces

    #Make a rectangle in each detected face.
    for(x, y, v1, v2) in face:
        #v1 and v2 = vertex1 and vertex2
        cv.rectangle(capture, (x, y), (x+v1, y+v2), (150,0,200), 1)
        capturedFace = captureId[y:y+v1, x:x+v2]
        capturedFace = cv.resize(capturedFace, (160,160), interpolation=cv.INTER_CUBIC)
        cv.imwrite(fullpath + '/image_{}.jpg'.format(imageId), capturedFace)
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(capture, f"Capture #{imageId}", (x, y-10), cv.FONT_HERSHEY_SIMPLEX, .75, color, 1)
        imageId += 1

    cv.imshow("Result", capture) 

    # Conditions to end scan
    if cv.waitKey(1) == ord('q'):
        break
    if imageId == 500:
        break

camera.release()
cv.destroyAllWindows()