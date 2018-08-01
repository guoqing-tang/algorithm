# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/17


'''简述：要求输入某年某月某日 提问：求判断输入日期是当年中的第几天？'''
year = int(input('请输入年份：'))
month = int(input('请输入月份：'))
day = int(input('请输入日期：'))
if day >31:
    print ('请正确输入')
if month > 12:
    print('请正确输入')
list1 = [31,59,90,130,151,181,212,243,273,304,334]
if (year % 4) == 0 or (year % 100) == 0 or (year % 400) == 0 and month >= 2:
    data = list1[month - 2] + day +1
if month == 1:
    data = day
if month == 2:
    data = 31 + day
print("这一天是这一年第"+str(data)+"天")
