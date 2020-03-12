import sys
from test import sendline
from send_pic import notifyFile
import cv2, sys, numpy, os
from datetime import date, datetime, timedelta
import mysql.connector
from inset_db import check_day1
from time_Check import check_time


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="12345678",
  database="empdb"
)
def convertTuple(tup): 
    str =  ''.join(tup) 

    return str


def check_name(name,date,time,im,g,status):
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id_student FROM student")
    myresult = mycursor.fetchall()
    
    for y in myresult:

        d=convertTuple(y)
        if d==name:
            g=0
            break
        elif d != name:
            g=1   

    if g==1:
       
        check_day1(name,date,time,im,status)