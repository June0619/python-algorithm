import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())
str_n = str(n)
stack = []

deleted_number = 0
for data in str_n:
    # 필요 없는 분기
    # if len(stack) == 0:
    #     stack.append(data)
    # else:
    # len 을 사용하지 않고 stack 객체 자체를 넣으면 원소가 있다는 조건문이 완성 됨
    while stack and int(data) > int(stack[-1]) and deleted_number != m:
        stack.pop()
        deleted_number += 1
    stack.append(data)

if deleted_number < m:
    for _ in range(m - deleted_number):
        stack.pop()
        deleted_number += 1

print(''.join(stack))

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)