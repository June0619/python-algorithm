import sys
# sys.stdin = open('input.txt', 'rt')

# input
n, m = map(int, input().split())

# 주사위 눈 합 모든 경우의 수 list append
sum_list = []
for i in range(1, n+1):
    for j in range(1, m+1):
        sum_list.append(i+j)

# 경우의 수 중복 제거
sum_set = set(sum_list)

# 합과 경우의 수를 정리하기 위한 dict 선언
answer_dict = dict()

# 중복을 제거한 주사위 눈의 합 경우의 수를 count 하여서 dict 에 key value 로 저장
for num in sum_set:
    if sum_list.count(num) not in answer_dict:
        answer_dict[sum_list.count(num)] = []
    answer_dict[sum_list.count(num)].append(num)

# 가장 높은 경우의 수를 가진 합 리스트 저장, 정렬
answer_list = answer_dict[max(list(answer_dict.keys()))]
answer_list.sort()

# 출력
for i in answer_list:
    print(i, end=' ')