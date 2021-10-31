import sys
import time
import itertools as it
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, f = map(int, input().split())

b = [1]*n

for i in range(1, n):
    b[i] = b[i-1] * (n-i) / i

a = list(range(1, n+1))
for tmp in it.permutations(a):
    summary = 0
    for L, x in enumerate(tmp):
        summary += (x * b[L])
    if summary == f:
        for x in tmp:
            print(x, end=' ')
        break


# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
