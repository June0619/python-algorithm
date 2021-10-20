import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()


def DFS(L, summary):

    if L == n and summary == f:
        for x in p:
            print(x, end=' ')
        print()
        print('수행시간 : ', time.time() - start_time)
        sys.exit(0)
    else:
        for j in range(1, n + 1):
            if ch[j] == 0:
                ch[j] = 1
                p[L] = j
                DFS(L + 1, summary + (p[L] * b[L]))
                ch[j] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)

    # nCr 콤비네이션 구하는 로직
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i

    DFS(0, 0)




