import cv2
import numpy as np
img = cv2.imread("cat1.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("image",gray)
# blur=cv2.GaussianBlur(gray,(7,7),cv2.BORDER_DEFAULT)
# canny=cv2.Canny(blur,127,170)
# cv2.imshow("canny",canny )
ret,trash=cv2.threshold(gray,127,220,type=cv2.THRESH_BINARY)

blank=np.zeros(img.shape,dtype='uint8')
countours,hararies=cv2.findContours(trash,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(blank, countours,-1,(0,0,255),2)
cv2.imshow("blank",blank )
print(f'{len(countours)} is found')
cv2.waitKey(0)