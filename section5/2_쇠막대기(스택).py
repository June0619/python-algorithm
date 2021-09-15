import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

inputs = input()
stack = []
answer = 0
last_txt = None

for i in inputs:
    if i == '(':
        stack.append(i)
    else:
        if last_txt == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

    last_txt = i

print(answer)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)