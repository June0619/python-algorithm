import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

prefix = input()
stack = []
temp = 0

for i in prefix:
    if i.isdecimal():
        stack.append(i)
    else:
        if i == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif i == '-':
            stack.append(-int(stack.pop()) + int(stack.pop()))
        elif i == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif i == '/':
            stack.append(int(stack.pop()) / int(stack.pop()))

print(stack.pop())

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)