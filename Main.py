import cv2
image = cv2.imread('contorno.jpg')# Get image
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Apply gray filter
umbral,umbralImage = cv2.threshold(grayImage, 50, 255, cv2.THRESH_BINARY) # Umbral
contours,jerarquia = cv2.findContours(umbralImage, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contoursColor = (0,255,0)

cv2.drawContours(image, contours, -1, contoursColor, 3)
# Show
cv2.imshow('Image', image)
# cv2.imshow('Gray Image', grayImage)
# cv2.imshow('Umbral Image', umbralImage)
cv2.waitKey(0)
cv2.destroyAllWindows()