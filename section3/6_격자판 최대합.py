import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

"""
모든 경우의 수(합) 을 구해서 max 를 비교하는 로직밖에 안떠오름 (방법 자체는 맞을 듯?) 
소스가 좀 난잡해지는 듯 함...

반복문을 한번만 돌 수 있는데 굳이 한번 더돌아서 시간복잡도가 두배로 늘어남...
"""

n = int(input())
# matrix = []
#
# for _ in range(n):
#     temp = list(map(int, input().split()))
#     matrix.append(temp)

# 위 소스 한줄로 합치기
matrix = [list(map(int, input().split())) for _ in range(n)]

max_value = 0

# 1. 모든 열 숫자 합 비교
# for one in matrix:
#     if sum(one) > max_value:
#         max_value = sum(one)
#
# # 2. 모든 행 숫자 합 비교
# for i in range(n):
#     temp_sum = 0
#     for j in range(n):
#         temp_sum += matrix[j][i]
#
#     if temp_sum > max_value:
#         max_value = temp_sum
# 1번과 2번 과정 합치기
for i in range(n):
    temp_sum1 = 0
    temp_sum2 = 0
    for j in range(n):
        temp_sum1 += matrix[i][j]
        temp_sum2 += matrix[j][i]

    if temp_sum1 > max_value:
        max_value = temp_sum1
    if temp_sum2 > max_value:
        max_value = temp_sum2

# 3. 첫 번째 대각선 합 비교
# temp_sum = 0
# for i in range(n):
#     temp_sum += matrix[i][i]
#
# if temp_sum > max_value:
#     max_value = temp_sum
#
# # 4. 두 번째 대각선 합 비교
# temp_sum = 0
# for i in range(n-1, -1, -1):
#     temp_sum += matrix[i][i]
#
# if temp_sum > max_value:
#     max_value = temp_sum

# 3번 과정과 4번 과정 합치기
temp_sum1 = 0
temp_sum2 = 0
for i in range(n):
    temp_sum1 += matrix[i][i]
    temp_sum2 += matrix[i][n-1-i]

if temp_sum1 > max_value:
    max_value = temp_sum1
if temp_sum2 > max_value:
    max_value = temp_sum2

print(max_value)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
# 내가 짠 소스 수행시간 :  0.001995563507080078
# 반복문 합친 소스 수행시간 :  0.001020669937133789