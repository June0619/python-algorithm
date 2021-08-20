import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

"""
1. 본질은 N*N 격자판에서 다이아몬드 그리기에 가까운 문제인 것 같음
2. 0번째 열의 가장 정 중앙(마름모의 꼭짓점) 부터 시작해서 넓이가 1칸씩 넓어진다는것을 주목
"""

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

lt = (n // 2)
rt = (n // 2)

summary = 0

for i in range(n):

    # for j in range(n):
    #     if lt <= j <= rt:
    #         summary += matrix[i][j]

    # 위 소스에서 쓸데 없는 탐색을 줄이도록
    for j in range(lt, rt+1):
        summary += matrix[i][j]

    if i < n // 2:
        lt -= 1
        rt += 1
    else:
        lt += 1
        rt -= 1

print(summary)

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)