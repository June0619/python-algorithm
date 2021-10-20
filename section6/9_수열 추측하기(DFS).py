import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, final_number = map(int, input().split())
number_list = list(range(1, n + 1))


def dfs(x):
    global param_arr
    if len(x) < n:
        for i in range(n):
            if number_list[i] not in x:
                dfs(x + [number_list[i]])
    else:
        result = 0
        for j in range(n):
            result += param_arr[j]*x[j]
        if result == final_number:
            for k in x:
                print(k, end=' ')
            sys.exit(0)
        return


def arrDFS(arr):

    if len(arr) < n:
        temp = [1]
        for i in range(len(arr) - 1):
            temp.append(arr[i] + arr[i + 1])
        else:
            temp.append(1)
        return arrDFS(temp)
    else:
        return arr


if __name__ == "__main__":
    param_arr = arrDFS([1])
    dfs([])


# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
