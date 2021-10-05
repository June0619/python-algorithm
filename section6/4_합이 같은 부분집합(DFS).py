import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())
input_list = list(map(int, input().split()))


def dfs(x, node):
    chk = 0
    if x > n-1:
        sum1 = sum(node)
        sum2 = 0
        for i in input_list:
            if i not in node:
                sum2 += i
        if sum1 == sum2:
            ch[0] += 1
    else:
        dfs(x + 1, node + [input_list[x]])
        dfs(x + 1, node)


ch = [0]
dfs(0, [])
if ch[0] > 0:
    print('YES')
else:
    print('NO')

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
