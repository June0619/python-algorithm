import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

'''
1. 명령어를 적용하는 함수 (인자1 = 행렬, 인자2 = 명령어 리스트)

2. 피라미드 영역 값 구하는 로직
'''


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


def rotate_matrix(p_matrix, p_command):
    line_idx = p_command[0] - 1
    direction = p_command[1]
    distance = p_command[2]

    rotate_line = p_matrix[line_idx]
    rotated_line = [0 for _ in range(len(rotate_line))]

    for i in enumerate(rotate_line):
        # 이동 방향이 왼쪽
        if direction == 0:
            # 일반적으로 왼쪽으로 거리만큼 이동하는 경우
            if i[0] - distance >= 0:
                rotated_line[i[0] - distance] = i[1]
            # 한바퀴 완전 회전하여 오른쪽 끝으로 이동하는 경우
            else:
                rotated_line[i[0] - distance + n] = i[1]
        else:
            # 일반적으로 오른쪽 거리만큼 이동하는 경우
            if i[0] + distance <= n-1:
                rotated_line[i[0] + distance] = i[1]
            # 한바퀴 완전 회전하여 오른쪽 끝으로 이동하는 경우
            else:
                rotated_line[i[0] + distance - n] = i[1]

    # 파라미터 행렬의 해당 열을 교환 해준다.
    p_matrix[line_idx] = rotated_line


m = int(input())
for _ in range(m):
    command = list(map(int, input().split()))

    rotate_matrix(matrix, command)

# for temp in matrix:
#     for j in temp:
#         print(j, end=' ')
#     print()

# 여기서 부터 다이아몬드 행렬의 합을 구해보자.
middle_idx = n // 2
lt = 0
rt = n
summary = 0

for j in range(n):
    # 중간 라인을 넘기 전 -> 왼쪽 오른쪽 영역 좁혀짐
    for k in matrix[j][lt:rt]:
        summary += k

    if j < middle_idx:
        lt += 1
        rt -= 1
    else:
        lt -= 1
        rt += 1

print(summary)

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
