import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())
graph = [[0] * n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    # 무방향이기 때문에 n, n 선을 기준으로 대칭이다.
    graph[a][b] = 1
    graph[b][a] = 1

for i in graph:
    for j in i:
        print(j, end=' ')
    print()

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
