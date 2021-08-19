"""
import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')
start_time = time.time()

'''
날먹 코드로 짜면..

당연히 안되겠지...? ㅜ_ㅜ

합친 다음 버블정렬로 구현하자....
'''

n = int(input())

list_1 = list(map(int, input().split()))

m = int(input())

list_2 = list(map(int, input().split()))

solution_list = list_1 + list_2

for i in range(len(solution_list)):
    for j in range(i+1, len(solution_list)):
        if solution_list[i] > solution_list[j]:
            solution_list[i], solution_list[j] = solution_list[j], solution_list[i]

for idx in solution_list:
    print(idx, end=' ')




# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)

"""

import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

'''
문제를 잘 읽어보자

두 개의 리스트 모두 오름차순으로 들어오기 때문에 시간복잡도를 확 줄일 수 있는 문제였다 ㅜ_ㅜ
'''
n = int(input())
list_1 = list(map(int, input().split()))
m = int(input())
list_2 = list(map(int, input().split()))

idx_1 = 0
idx_2 = 0

result_list = []

for _ in range(len(list_1) + len(list_2)):
    if list_1[idx_1] >= list_2[idx_2]:
        result_list.append(list_2[idx_2])
        idx_2 += 1
    elif list_2[idx_2] > list_1[idx_1]:
        result_list.append(list_1[idx_1])
        idx_1 += 1

    if idx_1 == len(list_1):
        result_list = result_list + list_2[idx_2::]
        break
    elif idx_2 == len(list_2):
        result_list = result_list + list_1[idx_1::]
        break

for i in result_list:
    print(i, end=' ')

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
