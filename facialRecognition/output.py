import cv2 as cv
import os

dataPath = "data"
dataList = os.listdir(dataPath)
trainingModel = cv.face.EigenFaceRecognizer_create()
trainingModel.read('training_EigenFaceRecognizer.xml')
noises = cv.CascadeClassifier('/home/gonzalo90fa/Desktop/Development projects/Curso Python 1/facialRecognition/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
# camera = cv.VideoCapture(0)
# camera = cv.VideoCapture('auron.jpg')
camera = cv.VideoCapture('ElonMusk.mp4')
color = (150,0,200)
while True:
    response,capture = camera.read()
    # response, capture = True, cv.imread('auron.jpg')
    if response == False: break
    grays = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)
    captureId = grays.copy()
    face = noises.detectMultiScale(grays, 1.9, 1)
    
    #Make a rectangle in each detected face.
    for(x, y, v1, v2) in face:
        #v1 and v2 = vertex1 and vertex2
        capturedFace = captureId[y:y+v1, x:x+v2]
        capturedFace = cv.resize(capturedFace, (160,160), interpolation=cv.INTER_CUBIC)
        result = trainingModel.predict(capturedFace)
        if result[1] <= 10000:
            cv.putText(capture, f"Result: {dataList[result[0]]}", (x, y-20), cv.FONT_HERSHEY_SIMPLEX, .75, color, 1)
        else:
            cv.putText(capture, "No reconocido", (x, y-20), cv.FONT_HERSHEY_SIMPLEX, .75, color, 1)
        cv.putText(capture, f"Result: {result}", (x, y-5), cv.FONT_HERSHEY_SIMPLEX, .35, color, 1)
        cv.rectangle(capture, (x, y), (x+v1, y+v2), color, 2)

    cv.imshow("Capture", capture)
    if cv.waitKey(1) == ord('q'):
        break
camera.release()
cv.destroyAllWindows()