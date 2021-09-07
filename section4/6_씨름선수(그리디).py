import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())
input_list = [tuple(map(int, input().split())) for _ in range(n)]


'''
input_list.sort()
cnt = 0

이런식으로 2중 for 문을 돌며 구현하는 것은 너무 비효율적임 반복문 한번으로 처리하는 코드로 변경
for i in range(n - 1):
    for j in range(i + 1, n):
        if input_list[i][1] < input_list[j][1]:
            cnt += 1
            break
'''

input_list.sort(reverse=True)
# 키가 가장 큰 선수는 무조건 선발 되기 때문에 카운트 1부터 시작함
cnt = 1
# 첫 번째 선수의 몸무게 (몸무게의 최댓값이 갱신 될 변수)
max_height = input_list[0][1]

for i in range(1, n):
    if input_list[i][1] > max_height:
        max_height = input_list[i][1]
        cnt += 1

# print(n - cnt)
print(cnt)

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
