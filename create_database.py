#creating database
import cv2, sys, numpy, os
from inset_db import insertdb
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
def create_data(student_id,firstname,lastname,year):
        
        webcam = cv2.VideoCapture(0) #'0' is use for my webcam, if you've any other camera attached use '1' like this
        sub_data='teaw'
        haar_file = 'haarcascade_frontalface_default.xml'
        datasets = 'datasets'  #All the faces data will be present this folder
             #This will creater folders in datasets with the face of people, so change it's name everytime for the new person.

        path = os.path.join(datasets, sub_data)
        if not os.path.isdir(path):
            os.mkdir(path)
        (width, height) = (130, 100)    # defining the size of images 


        face_cascade = cv2.CascadeClassifier(haar_file)
          

        # The program loops until it has 30 images of the face.
        count = 1
        while count < 50: 
            (_, im) = webcam.read()

            
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 4)
            for (x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (100, 100))
                cv2.imwrite('%s/%s.png' % (path,count), face_resize)
            count += 1
            frame75 = rescale_frame(im, percent=10)

            cv2.imshow('OpenCV', im)
            if cv2.waitKey(25) & 0xFF == ord('q'):
            
                cv2.destroyAllWindows()
                break
    
