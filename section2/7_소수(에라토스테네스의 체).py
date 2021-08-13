import sys
import time

# sys.stdin = open('input.txt', 'rt')

start_time = time.time()

# input
n = int(input())


def prime_check(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


# 하나씩 소수인지 체크하는 로직 (시간 초과 될 수밖에 없음)
# prime_numbers = []
#
# for i in range(2, n + 1):
#     if prime_check(i):
#         prime_numbers.append(i)
#
# print('time : ' + str(time.time() - start_time))
# print(len(prime_numbers))

# 에라토스테네스의 체를 이용하는 로직
prime_numbers = [0] * (n+1)
prime_count = 0

for i in range(2, len(prime_numbers)):
    if prime_numbers[i] == 0:
        prime_count += 1
        for j in range(i, n+1, i):
            prime_numbers[j] += 1

# print('time : ' + str(time.time() - start_time))
print(prime_count)