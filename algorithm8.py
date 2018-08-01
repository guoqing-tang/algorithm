# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/19
'''输出本地时间并停顿一秒，主要用到%格式'''
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# 暂停一秒
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))