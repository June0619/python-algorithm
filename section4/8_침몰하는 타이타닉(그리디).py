import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())
inputs = list(map(int, input().split()))

inputs.sort(reverse=True)
lt = 0
rt = n-1
cnt = 0
while rt >= lt:
    # 가장 무거운 승객과 가장 가벼운 승객이 구명보트 탈 수 있음
    if inputs[lt] + inputs[rt] <= m:
        lt += 1
        rt -= 1
        cnt += 1
    # 가장 무거운 승객만 탈 수 있음
    else:
        lt += 1
        cnt += 1

print(cnt)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)