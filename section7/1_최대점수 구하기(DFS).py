# import sys
# import time
# import random as r
#
# sys.stdin = open('input.txt', 'rt')
# start_time = time.time()
#
# n, m = map(int, input().split())
# solution_list = [tuple(map(int, input().split())) for _ in range(n)]
#
#
# def dfs(x, t, score):
#     global max_score
#
#     if x == n:
#         return
#
#     # 시간초과인 경우
#     if t + solution_list[x][1] > m:
#         return
#     else:
#         score += solution_list[x][0]
#         t += solution_list[x][1]
#
#         if score > max_score:
#             max_score = score
#
#     for i in range(x, n):
#         dfs(i + 1, t, score)
#
#
# if __name__ == '__main__':
#     max_score = 0
#     for k in range(n):
#         dfs(k, 0, 0)
#
#     print(max_score)
#
# # 수행시간 체크
# print('수행시간 : ', time.time() - start_time)

import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()


def dfs(x, score, t):
    global max_score

    if t > m:
        return

    if x == n:
        if score > max_score:
            max_score = score

    else:
        # 문제를 푼 경우 -> 점수와 소요시간에 현재 문제의 시간을 더한다.
        dfs(x+1, score + score_list[x], t + time_list[x])
        # 문제를 풀지 않고 넘어간 경우 -> 트리의 레벨만 1 증가시킨다.
        dfs(x+1, score, t)


if __name__ == '__main__':

    n, m = map(int, input().split())

    score_list = []
    time_list = []

    for i in range(n):
        a, b = map(int, input().split())
        score_list.append(a)
        time_list.append(b)

    max_score = 0
    dfs(0, 0, 0)

    print(max_score)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
