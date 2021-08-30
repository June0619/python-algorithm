import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

matrix = [list(map(int, input().split())) for _ in range(9)]

'''
일단 잘 모르겠으니 나눠서 전체를 탐색하는 느낌으로 해보자
1. 행 탐색
2. 열 탐색
3. 행 단위로 이동하면서 3x3 영역만 찾아서 탐색

스도쿠 조건
1. 가로 세로 대각선 모두 1부터 9의 숫자로 이루어 져 있음
-> 바꿔 말하면 가로 세로 대각선 영역에서 1~9 의 숫자가 '중복 없이' 존재함

강의 추가내용
1. set 을 쓰지 말고 배열을 이용해 파악하기
2. 이전 내용과 마찬가지로 행 탐색과 열 탐색은 같이 할 수 있었을 듯
'''

answer = None

# # 1. 행 탐색
# for temp_w in matrix:
#     # 중복 체크 할 set 객체 선언
#     # temp_set = set()
#     chk = [0 for _ in range(9)]
#
#     for i in temp_w:
#         # temp_set.add(i)
#         chk[i-1] = 1
#
#     # if len(temp_set) != 9:
#     if sum(chk) != 9:
#         answer = 'NO'

# 1. 행 탐색 & 열 탐색
for i in range(len(matrix)):
    # temp_set = set()
    chk1 = [0 for _ in range(9)]
    chk2 = [0 for _ in range(9)]
    for j in range(len(matrix)):
        # temp_set.add(matrix[j][i])
        chk1[matrix[i][j]-1] = 1
        chk2[matrix[j][i]-1] = 1

    # if len(temp_set) != 9:
    #     answer = 'NO'
    if sum(chk1) != 9 or sum(chk2) != 9:
        answer = 'NO'

# 3. 3x3 탐색
# for range_w in [range(0, 3), range(3, 6), range(6, 9)]:
#     for range_h in [range(0, 3), range(3, 6), range(6, 9)]:
#         # temp_set = set()
#         chk3 = [0 for _ in range(9)]
#         for i in range_w:
#             for j in range_h:
#                 # temp_set.add(matrix[i][j])
#                 chk3[matrix[i][j]-1] = 1
#         # if len(temp_set) != 9:
#         #     answer = 'NO'
#         if sum(chk3) != 9:
#             answer = 'NO'

# 3. 강사님 로직
for i in range(3):
    for j in range(3):
        chk3 = [0]*10
        for k in range(3):
            for s in range(3):
                chk3[matrix[i*3+k][j*3+s]] = 1
        if sum(chk3) != 9:
            answer = 'NO'

if answer is None:
    answer = 'YES'

print(answer)
# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)