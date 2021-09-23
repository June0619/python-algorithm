import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

tc = int(input())
words = dict()

for _ in range(tc):
    words[input()] = 0

for _ in range(tc-1):
    words[input()] += 1

# for i in words:
#     if words[i] == 0:
#         print(i)
# dictionary 자료형에서 key 와 value 를 한번에 출력하는 방법
for key, val in words.items():
    if val == 0:
        print(key)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)