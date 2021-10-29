import cv2
import numpy as np
import time
def draw2(frame,co,pt1,pt2):
        frame= cv2.resize(frame, (1080,720))
        top_left_corner_coordinates= pt1
        bottom_right_corner_coordinates= pt2
        color= co
        thickness=2
        frame=cv2.rectangle(frame, top_left_corner_coordinates,bottom_right_corner_coordinates,color,thickness)
        cv2.imshow("image",frame)
        return frame
def click_event(event,x,y,flag,perm):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY=str(x)+',  '+str(y)
        cv2.putText(img,strXY,(x,y),font,.5,(255,255,0),1)
        cv2.imshow("image",img)
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green = img[ x, y, 1]
        red = img[ x, y, 2]
        print(x, ', ', y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(blue) + ', ' + str(green)+', '+str(red)
        cv2.putText(img, strXY, (x, y), font, 1, (0,255, 255), 3)
        cv2.imshow("image", img)
pt1=(200,160)
pt2=(880,560)
co=(0,255,0)
img=cv2.imread('cat1.jpg')
#blank[::]=255,255,255  
#cv2.rectangle(blank,(10,10),(250,250),(0,250,0),thickness=cv2.FILLED)
#cv2.rectangle(blank, (1248, 64), (1311, 191), (0,255,0), 2)

#cv2.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=3)
#cv2.setMouseCallback("image",click_event)
img2=draw2(img, co,pt1,pt2)
draw2(img2,(255,0,0),(220 ,180),(860,540))


cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()