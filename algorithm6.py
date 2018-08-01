# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/18

'''def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a
    print(a)'''
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)