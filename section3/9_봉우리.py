import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

# 보다 쉬운 처리를 위한 좌표연산 리스트 초기화 해놓기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# n x n 행렬을 n+2 x n+2 0으로 둘러싼 행렬로 만들기

# 행 확장
matrix.insert(0, [0 for _ in range(n)])
matrix.append([0 for _ in range(n)])

# 열 확장
for i in range(n+2):
    matrix[i].insert(0, 0)
    matrix[i].append(0)

count = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        # if matrix[i][j] > matrix[i-1][j] and matrix[i][j] > matrix[i+1][j] and matrix[i][j] > matrix[i][j-1] and
        # matrix[i][j] > matrix[i][j+1]: count += 1
        if all(matrix[i][j] > matrix[i+dx[k]][j+dy[k]] for k in range(4)):
            count += 1

print(count)

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
# 내꺼 수행시간 :  0.0009889602661132812
# 바뀐 수행시간 :  0.0029909610748291016
