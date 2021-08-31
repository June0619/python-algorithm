import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())

input_list = list(map(int, input().split()))

input_list.sort()

idx_s = 0
idx_e = n - 1
idx = (idx_s + idx_e) // 2
answer = 0
while True:
    idx = (idx_s + idx_e) // 2

    if input_list[idx] == m:
        answer = idx + 1
        break
    elif input_list[idx] > m:
        idx_e = idx
    else:
        idx_s = idx

print(answer)
# 수행시간 체크
print('수행시간 : ', time.time() - start_time)