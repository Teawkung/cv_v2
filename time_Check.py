from time import time, sleep
from datetime import datetime, timedelta
from inset_db import check_day1
from test import sendline
from send_pic import notifyFile
def check_time():
	nowtime = time()

	#Put your script here
	print("hello")
	x = 1
	for k in range(500):
	        x+=1
	        sleep(0.01)

	sec = timedelta(seconds=int(time()-nowtime))
	d = datetime(1,1,1)+sec
	now_status='สาย'
	print("DAYS:HOURS:MIN:SEC")
	print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))