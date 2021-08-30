import sys
import time
from collections import deque
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

matrix = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    deq_w = deque()
    deq_h = deque()
    for j in range(7):
        deq_w.append(matrix[i][j])
        deq_h.append(matrix[j][i])

        # 데큐에 인자가 다섯개 쌓인 시점
        if j >= 4:
            if deq_w[0] == deq_w[4] and deq_w[1] == deq_w[3]:
                cnt += 1
            if deq_h[0] == deq_h[4] and deq_h[1] == deq_h[3]:
                cnt += 1
            deq_w.popleft()
            deq_h.popleft()

print(cnt)
# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
