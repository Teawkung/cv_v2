import datetime
import mysql.connector

from test import sendline

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="12345678",
  database="empdb"
)
def check_name(name,time):
	mycursor = mydb.cursor()
	mycursor.execute("SELECT student_name FROM day1")
	myresult = mycursor.fetchall()
	for x in myresult:
	  print(x)
	  
	  sendline(name,time)
