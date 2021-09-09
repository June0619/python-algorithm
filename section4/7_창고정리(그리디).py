import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

length = int(input())
inputs = list(map(int, input().split()))
run = int(input())

inputs.sort(reverse=True)

answer = 0

# print(inputs)

while run > 0 and length > 1:
    # 가장 높은 곳에서 하나 빼서
    inputs[0] = inputs[0] - 1

    # 가장 낮은 곳에 하나 더한다
    inputs[-1] = inputs[-1] + 1

    # 세번째, 네번째 n번째 높은 경우의 수를 커버하지 못하므로 오류가 있는 논리임
    # # 가장 높은 곳이 다음 인덱스보다 작아지면 위치 교환
    # if inputs[0] < inputs[1]:
    #     inputs[0], inputs[1] = inputs[1], inputs[0]
    #
    # # 가장 낮은 곳이 그 전 인덱스보다 커지면 위치 교환
    # if inputs[-1] > inputs[-2]:
    #     inputs[-1], inputs[-2] = inputs[-2], inputs[-1]

    # 시간초과 뜰거같은데...? 안뜨네...?
    inputs.sort(reverse=True)

    # 실행횟수 1회 차감
    run -= 1

    # print(inputs)

# 가장 높은 곳과 낮은 곳의 차이
answer = inputs[0] - inputs[-1]

print(answer)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)