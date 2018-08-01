# * -- utf-8 -- *    # python3
# Author: Tang   Time:2018/4/17
def main():
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if i !=k and i !=j and j !=k:
                    print(i * 100 + j * 10 + k)
if __name__=='__main__':
    main()

#简述：这里有四个数字，分别是：1、2、3、4
# 提问：能组成多少个互不相同且无重复数字的三位数？各是多少？