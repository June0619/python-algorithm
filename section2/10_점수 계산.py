import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')
# start_time = time.time()


# 스코어 계산 함수
def recursive_pointer(param_list, param_stair, param_result):
    if param_list.pop(0) == 1:
        param_stair += 1
        param_result += param_stair
    else:
        param_stair = 0
    if len(param_list) == 0:
        return param_result
    else:
        return recursive_pointer(param_list, param_stair, param_result)


# input
n = int(input())
score_list = list(map(int, input().split()))

print(recursive_pointer(score_list, 0, 0))

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
