import cv2
from facenet_pytorch import MTCNN
import numpy as np



class facedetection(object):
     """class"""

     def __init__(self, mtcnn):
         self.mtcnn = mtcnn
     def draw(self,frame,boxes,prob,landmark):
        for box, prob, ld in zip(boxes,prob,landmark):
            cv2.rectangle(frame,(int(box[0]),int(box[1])),(int(box[2]),int(box[3])),(0,0,255),2)
            #print(type(boxes[0]))
            return frame
     def draw2(self,frame):
        frame= cv2.resize(frame, (1080,720))
        top_left_corner_coordinates= (200,160)
        bottom_right_corner_coordinates= (880,560)
        color= (0,255,0)
        thickness=1
        frame=cv2.rectangle(frame, top_left_corner_coordinates,bottom_right_corner_coordinates,color,thickness)
        mytuple=(frame,top_left_corner_coordinates,bottom_right_corner_coordinates)
        return mytuple

     def run(self):
         cap=cv2.VideoCapture(0)
         while True:
            isTrue,frame=cap.read()
            try:
                frame1=cv2.resize(frame, (1080,720))
                boxes,prob,landmark=self.mtcnn.detect(frame1,landmarks=True)
                newbox=tuple(boxes.reshape(1, -1)[0])
                mytuple=self.draw2(frame1)
                frame1=mytuple[0]
                if (min(newbox[0],newbox[2])>=min(mytuple[1][0],mytuple[2][0]) and  max(newbox[0],newbox[2])<=max(mytuple[1][0],mytuple[2][0])) and  (min(newbox[1],newbox[3])>=min(mytuple[1][1],mytuple[2][1]) and  max(newbox[1],newbox[3])<=max(mytuple[1][1],mytuple[2][1])):
                    frame1=self.draw(frame1,boxes,prob,landmark)
                    print("in the box")
            except:
                print("face not found")

                    

            cv2.imshow('vid',frame1)
            if cv2.waitKey(20) & 0xff==ord('d'):
                break
cv2.destroyAllWindows()
         
mtcnn=MTCNN()
obj=facedetection(mtcnn)
obj.run()

        
    
