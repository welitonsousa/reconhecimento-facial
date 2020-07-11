import cv2

cam = cv2.VideoCapture(0)
classificator = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while (True) :
    conected, image = cam.read()
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    facedetected = classificator.detectMultiScale(imageGray, scaleFactor = 1.5, minSize = (100, 100))

    for (x, y, width, heigth) in facedetected:
        cv2.rectangle(image, (x, y), (x + width, y + heigth), (0,0,255), 2)

    cv2.imshow("face", image)
    cv2.waitKey(1)

cam.release()
cv2.destroyAllWindows()