import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()


def dfs(x):
    if x == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[x] = 1
        dfs(x + 1)
        ch[x] = 0
        dfs(x + 1)


param = list()

if __name__ == '__main__':
    n = int(input())
    ch = [0] * (n + 1)
    dfs(1)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
