import sys
import time
import random as r
import math

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())
coins = list(map(int, input().split()))
change = int(input())

# 미리 내림차순 정렬 해놓는게 탐색 속도 향상에 도움이 됨
coins.sort(reverse=True)


def dfs(res):
    global answer

    # 이미 동전 갯수가 최솟값을 넘은 경우
    if answer < len(res):
        return

    # 남은 거스름돈 잔액에 최대금액 동전 갯수를 다 더해도 이미 최소횟수가 아닌경우
    if answer < len(res) + ((change - sum(res)) // max(coins)):
        return

    # 동전의 합이 거슬러 줄 금액을 초과한 경우
    if sum(res) > change:
        return
    # 동전의 합이 거슬러 줄 금액과 일치하게 된 경우
    if sum(res) == change:
        if len(res) < answer:
            answer = len(res)
    else:
        for i in range(n):
            dfs(res + [coins[i]])


if __name__ == '__main__':
    answer = math.inf
    dfs([])

    print(answer)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
