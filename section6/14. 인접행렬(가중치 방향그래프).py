import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())

matrix = [[0] * n for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    matrix[i-1][j-1] = k

for one in matrix:
    for two in one:
        print(two, end=' ')
    print()


# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
