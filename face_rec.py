import cv2, sys, numpy, os
from test import sendline
from inset_db import check_day1,create_data
from datetime import datetime, time,timedelta
from PIL import ImageGrab,Image,ImageDraw,ImageFont
from send_pic import _lineNotify,notifyPicture,notifyFile
from testsql import check_name
from check import check_name
from time_Check import check_time
from test_time import date_diff_in_Seconds

import asyncio



#ตั้งค่าเวลา status

def start_record():
    try:
        create_data()
    except:
        pass
    status='เข้าเรียน'
    date1= datetime.now() + timedelta(seconds=60)  #ตั้งเวลาถอยหลัง
    #date1 = datetime.strptime('2019-11-10 17:34:00', '%Y-%m-%d %H:%M:%S')
    #Current date
    dateTimeObj = datetime.now()
    hour_check=int(dateTimeObj.hour)
    date_check=int(dateTimeObj.minute)
    if hour_check>10:
        status="สาย"

    #===========================================================================================================
    def convertTuple(tup): 
        str =  ''.join(tup) 
        return str

    msg=''
    haar_file = 'haarcascade_frontalface_default.xml'
    datasets = 'datasets'


    img_counter = 0
    list=[]
    print('START')
   
    (images, labels, names, id) = ([], [], {}, 0)
    for (subdirs, dirs, files) in os.walk(datasets):
        for subdir in dirs:
            names[id] = subdir
            subjectpath = os.path.join(datasets, subdir)
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                label = id
                images.append(cv2.imread(path, 0))
                labels.append(int(label))
            id += 1
    (width, height) = (130, 100)


    (images, labels) = [numpy.array(lis) for lis in [images, labels]]

    model = cv2.face.LBPHFaceRecognizer_create()
    model.train(images, labels)

  
    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture("http://192.168.1.56:36230/videostream.cgi?user=admin&pwd=88888888")
    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            
            prediction = model.predict(face_resize)
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 255, 255), 3)
            
            if prediction[1]<100:

                cv2.putText(im,'%s - %.0f ' % (names[prediction[0]],prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(255, 255, 255))
                
                name='%s' % (names[prediction[0]])
                x=datetime.now()
                date2 = datetime.now()

                #if date_diff_in_Seconds(date2, date1)>0:
                #    status='สาย'
                time=(x.strftime("%X"))
                date=(x.strftime("%x"))
                
                #print(date_diff_in_Seconds(date2,date1))
                if name in list:
                    break
                elif name not in list:
                    list.append(name)
                    try:
                        check_day1(name,time,im,status)
                        print("PASS")
                        #check_name(name,date,time,im,1,status)
                    except:
                        pass
                

            else:
              cv2.putText(im,'Unknown',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
              
       
        cv2.imshow('OpenCV', im)

        if cv2.waitKey(25) & 0xFF == ord('q'):
           
            cv2.destroyAllWindows()
            break

start_record()


