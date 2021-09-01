# Capa oculta entrenamiento
import cv2 as cv
import os
import numpy as np
from time import time

dataPath = "data"
dataList = os.listdir(dataPath)

imageIds = []
facesData = []
imageId = 0
startTime = time()
for row in dataList:
    fullpath = dataPath + '/' + row
    for file in os.listdir(fullpath):
        imageIds.append(imageId)
        facesData.append(cv.imread(fullpath + '/' + file, 0))
    imageId += 1
    finalTime = time()
    totalTime = finalTime - startTime
    print(f"Row: {row}, Time: {totalTime}")


trainingModel = cv.face.EigenFaceRecognizer_create()
print("The training is started")
trainingModel.train(facesData, np.array(imageIds)) 
trainingModel.write('training_EigenFaceRecognizer.xml')
print("Training finish")

