import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())
numbers = list(range(1, n + 1))
ch = [0] * m


def DFS(L, x):
    global ch
    global cnt
    # 트리의 Level 이 주어진 m을 초과하면 return
    if L < m:
        # 전 Level 의 탐색지점보다 하나 높은 인덱스부터 탐색
        for i in range(x, n):
            ch[L] = numbers[i]
            # 지정한 뎁스에 도달하면 출력하고 return
            if L + 1 == m:
                for k in ch:
                    print(k, end=' ')
                print()
                cnt += 1
            DFS(L + 1, i + 1)
    else:
        return


if __name__ == '__main__':
    cnt = 0
    DFS(0, 0)
    print(cnt)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
