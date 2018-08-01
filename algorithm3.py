# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/17

import math
for i in range(100000):
    x = int(math.sqrt(i+100))
y = int(math.sqrt(i+268))
    if (x*x == i+100) and (y*y ==i+268):
        print(i)
'''简述：一个整数，它加上100和加上268后都是一个完全平方数 提问：请问该数是多少？'''