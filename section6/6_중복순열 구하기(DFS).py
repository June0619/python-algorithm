import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())


def dfs(x, res):
    global cnt
    temp = []
    if x > 0:
        temp = res + [x]

    if len(temp) < m:
        for i in range(1, n+1):
            dfs(i, temp)
    else:
        for j in temp:
            print(j, end=' ')
        print()
        cnt += 1


if __name__ == '__main__':
    cnt = 0
    dfs(0, [])
    print(cnt)
# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
