import sys
import time

sys.stdin = open('input.txt', 'rt')

start_time = time.time()


def prime_check(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


n = int(input())
prime_numbers = []

for i in range(2, n + 1):
    if prime_check(i):
        prime_numbers.append(i)

print('time : ' + str(time.time() - start_time))
print(len(prime_numbers))
