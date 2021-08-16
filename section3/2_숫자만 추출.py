import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')
# start_time = time.time()


def get_divisor(val):
    count = 0
    for i in range(1, val + 1):
        if val % i == 0:
            count += 1

    return count


input_string = input()

zero_ord = ord('0')
nine_ord = ord('9')

chain_string = ''
for char in input_string:
    if '0' <= char <= '9':
        chain_string += char

print(int(chain_string))
print(get_divisor(int(chain_string)))

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
