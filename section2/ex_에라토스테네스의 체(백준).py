import sys
import time
import random as r
"""
백준 2960번 에라토스테네스의 체 
https://www.acmicpc.net/problem/2960
"""
sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, k = map(int, input().split())
prime_list = list()
count = 0

# 1. 2부터 N까지 모든 정수를 적는다
number_list = list(range(2, n+1))

# 2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이를 P라고 하고 이는 소수이다.
while number_list:
    prime_number = number_list[0]

    # 3. P를 지우고, 아직 지우지 않은 P의 배수를 순서대로 지운다.
    for i in number_list:
        if i % prime_number == 0:
            number_list.remove(i)
            count += 1

            if count == k:
                print(i)
                break

# 4. 아직 모든 수를 지우지 않았다면 다시 2번 단계로 간다.


# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)