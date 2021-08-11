import sys

# sys.stdin = open('input.txt', 'rt')

arr = [5, 3, 7, 9, 2, 5, 2, 6]

# 파이썬에서 가장 큰 무한대값이 저장 된다
arr_min = float('inf')

for i in range(len(arr)):
    # 첫번쨰 변수에 들어갈 조건을 무조건 만족시키기 위해 무한대 값을 저장한 것
    # 문제의 조건에서 중복 값도 처리하도록 제시한 경우 크거나 같은 조건으로 사용
    if arr[i] < arr_min:
        arr_min = arr[i]

print(arr_min)