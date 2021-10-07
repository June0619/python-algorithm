import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())
input_list = list(map(int, input().split()))


def dfs(x, summary):
    if summary > total // 2:
        return
    if x == n:
        if summary == (total - summary):
            print("YES")
            sys.exit(0)
    else:
        dfs(x + 1, summary + input_list[x])
        dfs(x + 1, summary)


total = sum(input_list)
dfs(0, 0)
print('NO')

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
