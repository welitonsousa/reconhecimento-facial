import cv2
cam = cv2.VideoCapture(0)

while (True) :
    conected, image = cam.read()
    cv2.imshow("face", image)
    cv2.waitKey(1)
cam.release()
cv2.destroyAllWindows()