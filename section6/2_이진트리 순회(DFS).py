import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()


def dfs(v):
    if v > 7:
        return
    else:
        # 순회 하기 전 로직을 처리하면 전위순회
        print(v, end=' ')
        dfs(v * 2)
        # 순회 중 로직을 처리하면 중위순회
        dfs(v * 2 + 1)
        # 순회가 끝나고 로직을 처리하면 후위순회


if __name__ == "__main__":
    dfs(1)


