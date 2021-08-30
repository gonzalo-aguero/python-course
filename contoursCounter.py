import cv2
import numpy as np
valorGauss = 13
valorKernel = 7

image = cv2.imread('monedas2.jpg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gaussImage = cv2.GaussianBlur(grayImage, (valorGauss, valorGauss), 0) # Remove image noise
bordersImage = cv2.Canny(gaussImage, 60, 100) # Remove image noise final

kernel = np.ones((valorKernel, valorKernel), np.uint8)
cierre = cv2.morphologyEx(bordersImage, cv2.MORPH_CLOSE, kernel) # Remove uninteresting items
contours,jerarquia = cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Find and count elements
contoursColor = (0,255,0)
print(f"Monedas encontradas: {format(len(contours))}")


cv2.drawContours(image, contours, -1, contoursColor, 3)
cv2.imshow("Image", image)
# cv2.imshow("Gray image", grayImage)
# cv2.imshow("Gauss image", gaussImage)
# cv2.imshow("Borders image", bordersImage)
# cv2.imshow("Morph close", cierre)
cv2.waitKey(0)