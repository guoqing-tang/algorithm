# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/19

for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%2d" % (i, j, i * j), end="    ")

    print(" ")