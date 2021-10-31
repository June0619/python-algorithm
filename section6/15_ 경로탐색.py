import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())

matrix = [[0] * n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1


def dfs(x):
    global cnt
    if x+1 == n:
        cnt += 1
        return
    for y in range(n):
        # 1. 간선이 존재할 것
        # 2. 현재 탐색에서 방문한 노드가 아닐 것
        if matrix[x][y] != 0 and ch[y] != 1:
            # 다음 노드로 넘어가면서 현재 노드의 위치를 방문했던 위치로 체크한다.
            ch[x] = 1
            dfs(y)
    # 탐색이 끝나면 노드 방문기록 초기화
    ch[x] = 0


if __name__ == '__main__':

    # 방문한 경로를 체크하기 위한 배열
    ch = [0] * n
    # n 번째 노드에 도달한 횟수
    cnt = 0

    dfs(0)

    print(cnt)
# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
