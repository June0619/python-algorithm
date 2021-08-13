import sys
# sys.stdin = open('input.txt', 'rt')

# N, K 입력
n, k = map(int, input().split())

# 입력 숫자 리스트
input_number_list = list(map(int, input().split()))

# 잘못된 로직 1
# 중복 제거하는 로직은 set() 함수로 간편하게 처리 가능함
# temp = 0
# for i in input_number_list:
#     if i == temp:
#         input_number_list.remove(i)
#     else:
#         temp = i

# 잘못된 로직 2
# 세번 째 수만 교체하면 된다는 발상 자체가 오류임
# 반례)
# 10 9 8 7 1 의 경우 세 번째로 큰 수가 10 9 1이 아니고 9 8 7 임
# a = sum(input_number_list[0:k+2])
# b = sum(input_number_list[2:k+1])
#
# print(a-b)

# 올바른 로직
# 리스트 안의 합을 전부 구해서 중복 제거 뒤 정렬 -> k 번째로 큰 수 출력

result = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            result.add(input_number_list[i] + input_number_list[j] + input_number_list[m])

result = list(result)
result.sort(reverse=True)

print(result[k-1])