"""
시간초과 난 로직 (내가 짠거)
import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')
sys.setrecursionlimit(10**7)
start_time = time.time()

n, m = map(int, input().split())

number_list = list(map(int, input().split()))


def search_summary(list_param, count):
    summary = 0
    if list_param:
        for i in list_param:
            summary += i

            if summary == m:
                count += 1
	    break
            elif summary > m:
                break
        list_param.pop(0)

        return search_summary(list_param, count)

    else:
        return count


print(search_summary(number_list, 0))

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
"""
# 정상 통과 된 로직 (해설 코드)
import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())

a = list(map(int, input().split()))

lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
