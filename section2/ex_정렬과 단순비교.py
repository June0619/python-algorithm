import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')

a = list(range(1000000))
b = list(range(1000000))
r.shuffle(a)
r.shuffle(b)

a_start_time = time.time()

a.sort(reverse=True)
a_max_value = a[0]

# 수행시간 체크
print('a 수행시간 : ', time.time() - a_start_time)

b_start_time = time.time()

b_max_value = -1
for i in b:
    if i > b_max_value:
        b_max_value = i

print('b 수행시간 : ', time.time() - b_start_time)
