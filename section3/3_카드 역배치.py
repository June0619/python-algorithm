'''
날먹 코드
import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')
# start_time = time.time()

tc = 10
base_list = list(range(1, 21))

while tc > 0:

    a, b = map(int, input().split())

    temp_list = base_list[a-1:b]
    temp_list.reverse()

    base_list[a-1:b] = temp_list

    tc -= 1

# 수행시간 체크

for i in base_list:
    print(i, end=' ')

# print('수행시간 : ', time.time() - start_time)
'''

import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')
# start_time = time.time()

tc = 10
base_list = list(range(1, 21))

while tc > 0:

    a, b = map(int, input().split())
    interval = (b - a + 1) // 2
    '''
    2부터 12라고 가정 -> 5회
    2, 12
    3, 11
    4, 10
    5, 9
    6, 8
    7

    2부터 9라고 가정 -> 4회
    2, 9
    3, 8
    4, 7
    5, 6

    위치 사이의 카드 개수 // 2
    '''

    for _ in range(interval):
        base_list[a - 1], base_list[b - 1] = base_list[b - 1], base_list[a - 1]
        a += 1
        b -= 1

    tc -= 1

# 수행시간 체크

for i in base_list:
    print(i, end=' ')

# print('수행시간 : ', time.time() - start_time)
