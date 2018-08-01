# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/23
'''实现1,到100的相加，试比较两种方法的差别'''

a = 1
for i in range(1,100):
    a += (i+1)
    print(a)
#方法2
b = sum(range(1,101))
print(b)
