import sys
import time

sys.stdin = open('input.txt', 'rt')

start_time = time.time()

# input
n = int(input())
input_number_list = list(map(int, input().split()))


def prime_check(number):
    # 1이 들어오는지 잘 체크해야 함
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


# 문자열로 처리하는 로직
def reverse(number):
    list_number = list(str(number))
    list_number.reverse()
    reverse_number = int(''.join(map(str, list_number)))
    return reverse_number


# 정석 로직
def reverse_2(number):
    temp = number
    reverse_number = 0
    while temp > 0:
        reverse_number = reverse_number * 10 + (temp % 10)
        temp = temp // 10


for i in input_number_list:
    answer = reverse(i)
    if prime_check(reverse(i)):
        print(answer, end=' ')