import cv2
import numpy as np

img = cv2.imread("resieb4.jpg")
b,g,r=cv2.split(img)
# cv2.imshow("blue",b)
# cv2.imshow("green",g)
# cv2.imshow("red",r)
blank=np.zeros(img.shape[:2],dtype='uint8')
mergeb=cv2.merge([b,blank,blank])
mergeg=cv2.merge([blank,g,blank])
merger=cv2.merge([blank,blank,r])


cv2.imshow("imageb",mergeb)
cv2.imshow("imageg",mergeg)
cv2.imshow("imager",merger)
cv2.waitKey(0)