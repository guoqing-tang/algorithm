# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/17

import math

for i in range(45,10000):
    x = int(math.sqrt(i-45))
    y = int(math.sqrt(i+44))
    if (x*x == i-45) and (y*y == i+45):
        print(i)

'''一个自然数减去45及加上44都仍是完全平方数，求此数y。次算法有问题'''

