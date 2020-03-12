from datetime import datetime, time,timedelta
def date_diff_in_Seconds(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds
#Specified date
date1 = datetime.strptime('2019-11-10 17:34:00', '%Y-%m-%d %H:%M:%S')
#Current date
date2 = datetime.now()
print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
if date_diff_in_Seconds(date2, date1)>50:
	status='สาย'
date1= datetime.now() + timedelta(seconds=60)  
print(date1)