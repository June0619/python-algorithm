import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
m = int(input())


def DFS(L, x):
    global cnt
    for i in range(x, n):
        ch[L] = numbers[i]
        # 지정한 조합 개수만큼 뽑았다면 조건 체크
        if L == k - 1:
            if sum(ch) % m == 0:
                cnt += 1
        # 아니라면 탐색 Level 증가
        else:
            DFS(L + 1, i + 1)


if __name__ == "__main__":
    # m 으로 나누어지는 조합 카운트
    cnt = 0
    # 조합을 기록할 배열
    ch = [0] * k
    DFS(0, 0)
    print(cnt)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
