import cv2
import numpy as np

def sortPoints(points):
    n_points = np.concatenate([points[0], points[1], points[2], points[3]]).tolist()
    y_order = sorted(n_points, key = lambda n_points: n_points[1])
    x1_order = y_order[0:2]
    x1_order = sorted(x1_order, key = lambda x1_order: x1_order[0])
    x2_order  = y_order[2:4]
    x2_order = sorted(x2_order, key = lambda x2_order: x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

def alignment(image, width, height):
    alignedImage = None
    graysImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    umbralImage = cv2.threshold(graysImage, 100, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow("Umbral camera",umbralImage)
    contours = cv2.findContours(umbralImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:1]
    for c in contours:
        CLOSED = True
        epsilon = 0.01 * cv2.arcLength(c, CLOSED)
        approx = cv2.approxPolyDP(c, epsilon, CLOSED)
        if len(approx) == 4:
            points = sortPoints(approx)
            point1 = np.float32(points)
            point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            M = cv2.getPerspectiveTransform(point1, point2)
            alignedImage = cv2.warpPerspective(image, M, (width, height))
    return alignedImage




# Start
capture = cv2.VideoCapture(0)
while True:
    cameraType, camera = capture.read()
    if cameraType == False:
        print("Camera not found.")
        break
    
    imageA6 = alignment(camera, 500, 500)
    if imageA6 is not None:
        points = []
        graysImage = cv2.cvtColor(imageA6, cv2.COLOR_BGR2GRAY)
        blurImage = cv2.GaussianBlur(graysImage, (5, 5), 1)
        umbralImage = cv2.threshold(graysImage, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
        cv2.imshow("Scanned umbral image", umbralImage)
        contour = cv2.findContours(umbralImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imageA6, contour, -1, (0, 0, 255), 2)
        suma1 = 0.0
        suma2 = 0.0
        totalArea = 0.0
        for c in contour:
            area = cv2.contourArea(c)
            moments = cv2.moments(c)
            if moments['m00'] == 0:
                moments['m00'] = 1.0
            x = int(moments['m10'] / moments['m00'])
            y = int(moments['m01'] / moments['m00'])
            
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(imageA6, f"{area}px", (x, y), font, 0.75, (0, 255, 0), 1)
            totalArea += area
        print(f"Total area in px: {area}px ({len(contour)} elements)")
        cv2.imshow("Processed scanned image", imageA6)
        cv2.imshow("Scanned image", camera)
    if cv2.waitKey(1) == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()