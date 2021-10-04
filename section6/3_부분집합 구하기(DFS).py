import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())


def dfs(x, node):
    if x > n:
        for i in node:
            print(i, end=' ')
        if node:
            print()
        return
    else:
        dfs(x + 1, node + [x])
        dfs(x + 1, node)


param = list()

if __name__ == '__main__':
    dfs(1, param)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
