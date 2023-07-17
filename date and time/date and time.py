'''https://docs.python.org/3/library/datetime.html#id1'''
from time import time

start=time()

import datetime 
dat=datetime.datetime
print(dat.fromisocalendar(1970,53,7))
d1=datetime.timedelta(days=5, seconds=2500, microseconds=23008, milliseconds=25545, minutes=484, hours=5, weeks=6)
d2=datetime.timedelta(6,6848,6878,87368,369,4)
print(abs(d1-d2))
# import datetime

# year = 2023
# week_number = 29
# weekday = 1  # Monday

# # Create a time object with the desired time
# time = datetime.time(hour=12, minute=30, second=0)
# date=datetime.datetime.fromisocalendar(year, week_number, weekday)

# # Create the datetime object using fromisocalendar and combine with the desired time
# dt = datetime.datetime.fromisocalendar(year, week_number, weekday).combine(date=date,time=time)

# print(dt)

dt1,dt2 = datetime.datetime(2023,7,17,10,30,0), datetime.datetime(2023,7,6,5,32,6)
print(dt1-dt2)

td1,td2=datetime.timedelta(5,1254,52,8,65,6,6),datetime.timedelta(6,1523,45,6,22,6,4)
print(td1-td2)

print(datetime.timedelta().max.total_seconds())

print(datetime.datetime.today())

print(datetime.date.fromtimestamp(1689584662))
print(datetime.date.fromordinal(1400))

print(time())


end=time()
print('\nElapsed Time: '+str(end-start)+'seconds')

