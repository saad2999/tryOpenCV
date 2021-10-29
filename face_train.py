import os
import cv2
import numpy as np
from PIL import Image

people=['Ben Afflek','Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
DIR=r'C:\Users\Mian Maaz\Desktop\train\train'
features=[]
labels=[]
haar_cascade=cv2.CascadeClassifier("har.xml")
label=[]
def my_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        print(label)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv2.imread(img_path)
            if img_array is None:
                continue
            gray=cv2.cvtColor(img_array ,cv2.COLOR_BGR2GRAY)
            f_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.6,minNeighbors=4)
        for (x,y,w,h,) in f_rect:
            faces_roi=gray[y:y+h,x:x+w]
            features.append(faces_roi)
            labels.append(label)

my_train()
print('Training done ---------------')

features1 = np.array(features, dtype='object')
labels1 = np.array(labels)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels1)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels1)
for i in labels1:
    print(i)