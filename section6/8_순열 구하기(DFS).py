import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())


def dfs(x, res):
    global cnt

    if x > 0:
        # 중복 제거
        if x not in res:
            res = res + [x]
        else:
            return

    if len(res) < m:
        # 간선은 항상 n개 만큼 뻗어 나감
        for i in range(1, n + 1):
            dfs(i, res)
    else:
        for j in res:
            print(j, end=' ')
        print()
        # 경우의 수 체크
        cnt += 1


if __name__ == "__main__":
    cnt = 0
    dfs(0, [])
    print(cnt)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
