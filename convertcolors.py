import cv2
import numpy as np

img = cv2.imread("resieb4.jpg")

#bgr to hsv
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("image1",img)
#bgr to lab
lab=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("image",lab)

cv2.waitKey(0)