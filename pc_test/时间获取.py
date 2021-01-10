import datetime
# 获取当前时间, 其中中包含了year, month, hour, 需要import datetime

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)


# 使用datetime.now()
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)


# 取得当前时间戳
import time
print(time.time())


# 时间戳转时间对象：
print(time.localtime(time.time()))

print(datetime.datetime.fromtimestamp(time.time()))


# 格式化当前日期

print(datetime.datetime.now().strftime('%Y-%m-%d'))


# 格式化当前日期

print(time.strftime("%H:%M:%S")) ##24小时格式
print(time.strftime("%I:%M:%S")) ##12小时格式


# 字符串转datetime
string = '2018-10-29 11:59:58'
print(datetime.datetime.strptime(string,'%Y-%m-%d %H:%M:%S'))

# datetime转字符串
print(datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M:%S'))
