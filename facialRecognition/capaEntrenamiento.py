# Capa oculta entrenamiento
import cv2 as cv
import os
import numpy as np
dataPath = "data"
dataList = os.listdir(dataPath)

imageIds = []
facesData = []
imageId = 0
for row in dataList:
    fullpath = dataPath + '/' + row
    for file in os.listdir(fullpath):
        imageIds.append(imageId)
        facesData.append(cv.imread(fullpath + '/' + file, 0))
        imageId += 1

trainingModel = cv.face.EigenFaceRecognizer_create()
print("The training is started")
trainingModel.train(facesData, np.array(imageIds)) 
trainingModel.write('training_EigenFaceRecognizer.xml')

