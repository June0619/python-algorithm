import sys
import time
import random as r

# sys.stdin = open('input.txt', 'rt')
# start_time = time.time()

# test case input
tc = int(input())

for idx in range(1, tc+1):

    # string input
    input_string = input().lower()

    result = ''

    # 대칭이라고 가정하면 뒤에서부터 읽으면 됨
    for i in range(len(input_string)//2):
        if input_string[i] != input_string[-(i+1)]:
            result = 'NO'
            break
    else:
        result = 'YES'

    # 역슬라이싱 이용한 풀이 (직접 하는것도 중요함)
    # if input_string == input_string[::-1]:
    #     result = 'YES'
    # else:
    #     result = 'NO'

    print('#{0} {1}'.format(idx, result))


# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
