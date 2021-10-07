import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

max_weight, n = map(int, input().split())


def dfs(x, summary):

    global answer
    # cut-edge 1
    # 합이 이미 최대 무게를 넘은 경우
    if summary > max_weight:
        return
    # cut-edge 2
    # 이미 더해진 합 + 아직 가지 않은 간선의 모든 합 < 최대 무게인 경우
    if (summary + sum(input_list[x:n])) < answer:
        return
    if x == n:
        if summary > answer:
            answer = summary
            return
    else:
        dfs(x+1, summary + input_list[x])
        dfs(x+1, summary)


if __name__ == "__main__":
    input_list = []
    for _ in range(n):
        input_list.append(int(input()))

    total = sum(input_list)
    answer = 0
    dfs(0, 0)

    print(answer)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)

