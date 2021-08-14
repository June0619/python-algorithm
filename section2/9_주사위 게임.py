import sys
import time

# sys.stdin = open('input.txt', 'rt')

# start_time = time.time()

# input
n = int(input())
# 상금 담을 배열
price_list = []

# test case 반복
while n > 0:
    input_number_list = list(map(int, input().split()))

    # 상금 계산을 편리하게 하기 위해 정렬 한번 해두기
    input_number_list.sort()

    # case 1 - 주사위 눈이 다 같을 경우
    if input_number_list[0] == input_number_list[1] == input_number_list[2]:
        price_list.append(10000 + input_number_list[2] * 1000)
    # case 3 - 주사위 눈이 다 다를 경우
    elif input_number_list[0] != input_number_list[1] != input_number_list[2]:
        price_list.append(input_number_list[2] * 100)
    # case 2 - 주사위 눈이 두개만 같을 경우
    else:
        # O(n)의 시간복잡도를 가지지만 표본이 여섯개이므로 크게 문제되지 않을것 같다.
        for i in input_number_list:
            if input_number_list.count(i) == 2:
                price_list.append(1000 + 100*i)
                break

    n -= 1

price_list.sort(reverse=True)
print(price_list[0])

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
