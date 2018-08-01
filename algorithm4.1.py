# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/17

year = int(input("年份："))
month = int(input("月份:"))
day = int(input("日期:"))

months = [0,31,59,90,130,151,181,212,243,273,304,334]
if 0 < month <= 12:
    sum = months[month-1]
else:
    print("data error")
    sum +=day
leap = 0

if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    leap = 1
if (leap == 1) and (month > 2):
    sum +=1
print('it is the %dth day ' % sum)