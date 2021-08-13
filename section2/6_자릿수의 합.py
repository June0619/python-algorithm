import sys


# sys.stdin = open('input.txt', 'rt')


# definition digit_sum function
def digit_sum(x):
    return_value = 0
    tmp = x
    while tmp > 0:
        return_value += tmp % 10
        tmp = tmp // 10
    return return_value


# definition digit_sum function ver.2
def digit_sum_2(x):
    return_value = 0
    tmp = str(x)
    for i in tmp:
        return_value += int(i)
    return return_value


# input
tc = int(input())
numbers = list(map(int, input().split()))

# 자릿수의 합 최대값 저장할 변수
answer = 0

# 자릿수의 합 최대값 구하는 로직
for i in numbers:
    if digit_sum(i) > digit_sum(answer):
        answer = i

# 출력
print(answer)
