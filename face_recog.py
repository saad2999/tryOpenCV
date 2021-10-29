import cv2
import numpy as np
people=['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
haar_cascade=cv2.CascadeClassifier("har.xml")
#features=np.load("features.npy")
#labels=np.load("labels.npy")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

face_recognizer.read("face_trained.yml")
img=cv2.imread(r'C:\Users\Mian Maaz\Desktop\train\val\madonna/3.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("person",gray)
f_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
for (x,y,w,h,) in f_rect:
    faces_roi=gray[y:y+h,x:x+w]
label,cofidence=face_recognizer.predict(faces_roi)
print(f'labls={people[label]} with confidence {cofidence}')
cv2.putText(img,str(people[label]),(20,20),cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255,),thickness=2)
frame=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv2.imshow("person",img)
cv2.waitKey(0)