import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())
inputs = list(map(int, input().split()))
numbers = list(range(1, n + 1))

inputs.reverse()

#
for i in range(1, len(inputs)):
    moving = inputs[i]
    numbers_i = n-i-1
    if moving > 0:
        numbers.insert(numbers_i+moving, numbers.pop(numbers_i))

for n in numbers:
    print(n, end=' ')

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
