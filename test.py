
# 파이썬으로 배우는 알고리즘 트레이딩

def print_ntimes(n):
    for i in range(n):
        print('대신증권')


print_ntimes(1)
print_ntimes(3)

print('==========')


def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return upper_price

cal_upper(1000)

from random import *
print(random())
