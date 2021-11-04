import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()


def dfs(now, summary_income):
    global max_summary
    # N+1번째 날이 되면 끝난다.
    if now > n:
        if summary_income > max_summary:
            max_summary = summary_income
        return

    # CASE 1. 상담을 받는다.
    # CASE 2. 상담을 받지 않는다
    # 지정된 날짜를 초과하지 않아야 함
    if now + cost[now-1] <= n+1:
        dfs(now + cost[now-1], summary_income + income[now-1])
        dfs(now + 1, summary_income)
    else:
        dfs(now + 1, summary_income)


if __name__ == '__main__':
    n = int(input())
    max_summary = 0

    cost = []
    income = []

    for _ in range(n):
        a, b = map(int, input().split())
        cost.append(a)
        income.append(b)

    dfs(1, 0)
    print(max_summary)



# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
