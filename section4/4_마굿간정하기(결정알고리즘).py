import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')
start_time = time.time()


def count(distance):
    cnt = 1
    end_point = x_coordinate[0]
    for i in range(1, n):
        if x_coordinate[i] - end_point >= distance:
            cnt += 1
            end_point = x_coordinate[i]

    return cnt


n, c = map(int, input().split())
x_coordinate = []
for _ in range(n):
    x_coordinate.append(int(input()))

x_coordinate.sort()

lt = 1
rt = x_coordinate[-1]

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
