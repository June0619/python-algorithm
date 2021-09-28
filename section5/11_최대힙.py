import sys
import time
import random as r
import heapq as hq

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            # 꺼낼 때도 반대 부호로 꺼내야 함
            print(-hq.heappop(a))
    else:
        # 최소힙과 부호 반대
        hq.heappush(a, -n)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)