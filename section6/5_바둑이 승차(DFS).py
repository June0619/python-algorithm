import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

max_weight, n = map(int, input().split())


def dfs(x, node):
    if x == n:
        if sum(node) > max_weight:
            return
        else:
            if sum(node) > max_ch[0]:
                max_ch[0] = sum(node)
                return
    else:
        dfs(x+1, node+[input_list[x]])
        dfs(x+1, node)


if __name__ == "__main__":
    input_list = []
    for _ in range(n):
        input_list.append(int(input()))

    max_ch = [0]
    dfs(0, [])

    print(max_ch[0])

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)

'''
단순 dfs 로 구현하니 실행시간 초과됨... 
'''