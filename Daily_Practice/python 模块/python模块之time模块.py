import time


print(help(time)) # 打印帮助信息

print(time.time()) #1610720236.653394 # 打印当前时间戳

time.sleep(3) # 暂停3秒

print(time.gmtime()) # 结构化时间 time.struct_time(tm_year=2021, tm_mon=1, tm_mday=15, tm_hour=14, tm_min=22, tm_sec=30, tm_wday=4, tm_yday=15, tm_isdst=0)

print(time.localtime()) # 当前结构化时间

struct_time=time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) # 格式化时间


print(time.strptime("2021-01-15 22:26:28","%Y-%m-%d %H:%M:%S")) # 将格式化时间转变为结构化时间

a=time.strptime("2021-01-15 22:26:28","%Y-%m-%d %H:%M:%S")
print(a.tm_yday)
print(a.tm_wday)

print(time.ctime())
print(time.ctime(0))  # 将秒数转变为一个时间

print(time.mktime(time.localtime())) # 将结构化时间转化为时间戳

import datetime

print(datetime.datetime.now())