import cv2
import numpy as np
img =np.zeros((400,400),dtype="uint8")
rect=cv2.rectangle(img.copy(),(30,30),(370,370),255,-1)
circle=cv2.circle(img.copy(),(200,200),200,255,-1)
# cv2.imshow("rect",rect)
# cv2.imshow("circle",circle)

bitwise_and=cv2.bitwise_and(rect,circle)
cv2.imshow("bitwise_and",bitwise_and)
bitwise_or=cv2.bitwise_or(rect,circle)
cv2.imshow("bitwise_or",bitwise_or)
bitwise_xor=cv2.bitwise_xor(rect,circle)
cv2.imshow("bitwise_xor",bitwise_xor)
bitwise_not=cv2.bitwise_not(circle)
cv2.imshow("bitwise_not",bitwise_not)




cv2.waitKey(0)