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