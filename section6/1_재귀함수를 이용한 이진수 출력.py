import sys
import time
import random as r

start_time = time.time()

n = int(input())


def div_two(x):
    if x // 2 != 1:
        div_two(x // 2)
        print(x % 2, end='')
    else:
        print(x // 2, end='')
        print(x % 2, end='')


div_two(n)
