# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/17
'''从键盘获取x y z三位数，输出其中最大的'''

x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))
if x > y:
    c = x
else:
    c = y

if z > c:
    print(z)
else:
    print(c)
