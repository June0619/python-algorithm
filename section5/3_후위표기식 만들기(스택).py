import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

infix = input()

stack = []
answer = ''

for i in infix:
    # 숫자의 경우
    if i.isdecimal():
        answer += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()

print(answer)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)