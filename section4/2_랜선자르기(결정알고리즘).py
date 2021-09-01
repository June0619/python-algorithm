import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

k, n = map(int, input().split())
input_list = [int(input()) for _ in range(k)]

lt = 1
rt = sum(input_list) // n
mid = (lt + rt) // 2

while lt <= rt:
    cnt = 0
    for i in input_list:
        cnt += i // mid

    if cnt >= n:
        lt = mid+1
        mid = (lt + rt) // 2
    else:
        rt = mid-1
        mid = (lt + rt) // 2

print(mid)


# 수행시간 체크
print('수행시간 : ', time.time() - start_time)