import datetime

dt = datetime.datetime.today()
# print(dt)  # 2021-10-29 15:58:08.356501

print(f'year: {dt.year}, month: {dt.month}, day: {dt.day}')
print(f'hour: {dt.hour}, minute: {dt.minute}, second: {dt.second}')
print(f'micro second: {dt.microsecond}')
#year: 2021, month: 10, day: 29
#hour: 15, minute: 58, second: 8
#micro second: 356501

#import time

#t = time.time() 
#dt_from_timestamp = datetime.datetime.fromtimestamp(t)
#c_time = time.ctime(t) 
#print(c_time)
#local_time = time.localtime(t) 
#print(local_time)
#gm_time = time.gmtime(t) 
#print(gm_time)
#time.struct_time(tm_year=2021, tm_mon=10, tm_mday=29, tm_hour=16, tm_min=59,
# tm_sec=4, tm_wday=4, tm_yday=302, tm_isdst=0)
#time.struct_time(tm_year=2021, tm_mon=10, tm_mday=29, tm_hour=7, tm_min=59,
#tm_sec=4, tm_wday=4, tm_yday=302, tm_isdst=0)
