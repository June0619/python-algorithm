import sys

# sys.stdin = open('input.txt', 'rt')


# 정확한 의미의 소숫점 반올림 함수
def custom_round(val):
    return int(val + 0.5)


# INPUT
n = int(input())
numbers = list(map(int, input().split()))

# 평균
# round() 함수는 round_half_even 방식을 사용하고 있어서 정확히 중간값에서 짝수쪽으로 가까운 값을 준다. 정확한 반올림이라고 하기 어렵다.
average = custom_round(sum(numbers) / n)

min_num = 0  # 최소 수
min_gap = float('inf')  # 최소 차
for i in range(len(numbers)):
    # 절대값이 다른 경우 ( 더 가까워지는 경우 )
    if abs(numbers[i] - average) < abs(min_gap):
        min_gap = numbers[i] - average
        min_num = i + 1
    # 절대값이 같은 경우
    elif abs(numbers[i] - average) == abs(min_gap) and numbers[i] - average > min_gap:
        min_gap = numbers[i] - average
        min_num = i + 1

print(average, min_num)

# 인덱스 번호와 값을 함께 전달받으며 for 문 사용하는 법
# for idx, x in enumerate(numbers):