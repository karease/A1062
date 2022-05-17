import time


print(time.time())
#获取当地时间  返回的是结构化时间
print(time.localtime())
#获取UTC时间  返回的还是结构化时间  比中国时间少8 小时
print(time.gmtime())

#结构化时间转换成字符串时间
print(time.strftime('%Y-%m-%d %H:%M:%S'))

