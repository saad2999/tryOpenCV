import cv2
import numpy as np

img = cv2.imread("resieb4.jpg")
#cv2.imshow("image",img)
#averaging

avg=cv2.blur(img,(7,7))
#cv2.imshow("avg",avg)
gblur=cv2.GaussianBlur(img,(7,7),0 )
#cv2.imshow("gblur",gblur)
## midian blurr
med=cv2.medianBlur(img,7)
#cv2.imshow("median",med)
bilateral =cv2.bilateralFilter (img,5 ,15,15)
cv2.imshow("b",bilateral)

cv2.waitKey(0)