import sys
import time
import itertools as it
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())

cnt = 0

for x in it.combinations(a, k):
    if sum(x) % m == 0:
        cnt += 1

print(cnt)


# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
