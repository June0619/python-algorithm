import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())
inputs = list(map(int, input().split()))

lt = 0
rt = n - 1
max_value = 0
answer = ''

# 반복 조건
# 1. 배열의 모든 값이 소진되지 않았어야 함(rt >= lt)
# 2. lt rt 둘이 가르키는 값 중 하나는 최대값이어야 함
while lt <= rt:
    # 둘 다 대상일 경우 -> 값 비교해야 함
    if inputs[lt] > max_value and inputs[rt] > max_value:
        # 왼쪽 노드 값이 더 작은 경우 (마지막 하나 남았을때도 고려)
        if inputs[lt] <= inputs[rt]:
            max_value = inputs[lt]
            lt += 1
            answer += 'L'
        # 오른쪽 노드 값이 더 작은 경우
        else:
            max_value = inputs[rt]
            rt -= 1
            answer += 'R'
    # 오른쪽 노드의 값이 최대값보다 작아진 경우
    elif inputs[lt] > max_value > inputs[rt]:
        max_value = inputs[lt]
        lt += 1
        answer += 'L'
    # 왼쪽 노드의 값이 최대값보다 작아진 경우
    elif inputs[rt] > max_value > inputs[lt]:
        max_value = inputs[rt]
        rt -= 1
        answer += 'R'
    # 둘 다 작아진 경우
    else:
        break

print(len(answer))
print(answer)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)