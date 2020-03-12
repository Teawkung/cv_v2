
from concurrent.futures import ThreadPoolExecutor
import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta
import asyncio 
import datetime
import mysql.connector
import sys
from test import sendline
from send_pic import notifyFile
import cv2
from mysql.connector import errorcode
import threading

try:
    mydb = mysql.connector.connect(
      host="192.168.1.60",
      user="test",
      passwd="12345678",
      database="empdb"
    )
except:
    pass

global now_status
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str
def insertdb(myname):
    mycursor = mydb.cursor()
    myname='teaw'
    fullname=''
    sql = "INSERT INTO student(student_name,full_name) VALUES (%s,%s)"
    val = (myname,fullname)

    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def create_data():
    myDate = date.today()
    checkmonth =int(myDate.month)
    if checkmonth<10:
        month="0"+str(myDate.month)
    else:
        month=str(myDate.month)
    
    myDate.strftime("%d/%m/%y")    
    dateStr = "d"+ str(myDate.year) +month+str(myDate.day) 
    
    mycursor = mydb.cursor()        
    sql = """CREATE TABLE IF NOT EXISTS %s (id INT AUTO_INCREMENT PRIMARY KEY,student_id VARCHAR(20),status CHAR(22),time_come VARCHAR(20),date_come VARCHAR(20))""" % dateStr
    #mycursor.execute("CREATE TABLE 40 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
    mycursor.execute(sql)
    print(sql)

def run_io_tasks_in_parallel(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            running_task.result()


def check_day1(name,time,im,now_status):

    myDate = date.today()
    checkmonth =int(myDate.month)
    if checkmonth<10:
        month="0"+str(myDate.month)
    else:
        month=str(myDate.month)
        
    dateStr = "d"+ str(myDate.year) +month+str(myDate.day)
    g=1
    mycursor = mydb.cursor()
    sql = "SELECT student_id FROM %s" % dateStr
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    for y in myresult:
        d=convertTuple(y)
        if d==name:
            g=0
            break
        elif d != name:
            g=1   


    if g==1:
        img_name = "opencv_frame_{}.png".format(name)
        cv2.imwrite(img_name, im)
        print("{} written!".format(img_name))

        sql = "INSERT INTO "+dateStr + "(student_id,status,time_come,date_come) VALUES (%s,%s,%s,%s)"
        now_day=str(myDate)
        date_today=str(myDate.year) +"/"+month+"/"+str(myDate.day) 
        val=(name,now_status,time,date_today)
        
        sendline(name,time)
        #notifyFile(img_name)
        #notifyFile(img_name)


        mycursor.execute(sql,val)
        mydb.commit()
        print(name,time)
        print(mycursor.rowcount, "record inserted.")

"""myDate=date.today()
checkmonth =int(myDate.month)
if checkmonth<10:
    month="0"+str(myDate.month)
else:
    month=str(myDate.month)
date_today=str(myDate.year) +"/"+month+"/"+str(myDate.day) 
print(date_today)

myDate.strftime("%d/%m/%y")    
dateStr = "d"+ str(myDate.year) +month+str(myDate.day) 
mycursor = mydb.cursor()
sql = "SELECT student_id FROM %s" % dateStr
mycursor.execute(sql)
myresult = mycursor.fetchall()
print(type(myresult))
for y in myresult:
    x=str(y)
    print(x)"""
