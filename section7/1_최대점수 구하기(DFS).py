import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, m = map(int, input().split())
solution_list = [tuple(map(int, input().split())) for _ in range(n)]


def dfs(x, t, score):
    global max_score

    if x == n:
        return

    # 시간초과인 경우
    if t + solution_list[x][1] > m:
        return
    else:
        score += solution_list[x][0]
        t += solution_list[x][1]

        if score > max_score:
            max_score = score

    for i in range(x, n):
        dfs(i + 1, t, score)


if __name__ == '__main__':
    max_score = 0
    for k in range(n):
        dfs(k, 0, 0)

    print(max_score)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
