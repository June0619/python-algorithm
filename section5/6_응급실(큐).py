import sys
import time
import random as r
from collections import deque

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())
patients = list(map(int, input().split()))
deq = deque(enumerate(patients))
cnt = 0

while deq:
    temp = deq.popleft()
    if deq and temp[1] < max(deq, key=lambda x: (x[1], x[0]))[1]:
        deq.append(temp)
    else:
        cnt += 1
        if temp[0] == m:
            print(cnt)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)