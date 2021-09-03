import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

'''
1. 
최솟값(lt): 1
최대값(rt): 곡의 길이를 모두 합한 값
'''

n, m = map(int, input().split())
input_list = list(map(int, input().split()))
# 이거 정렬하면 안됨............................
# 곡의 트랙 순서는 다를 수 있으므로 정렬하면 절대 안됨...
# input_list.sort()
res = float('inf')

lt = max(input_list)
rt = sum(input_list)

while lt <= rt:
    mid = (lt + rt) // 2
    cnt = 1
    dvd = 0
    # 곡의 길이가 짧은 순서부터 DVD 에 녹화 됨
    for i in input_list:
        # 곡의 길이가 dvd 용량보다 크지 않을 때 까지 녹화
        if dvd + i <= mid:

            dvd += i
        # 곡의 길이가 dvd 용량보다 크면 다음 dvd 사용, 사용한 dvd 카운트 갯수 + 1
        else:
            dvd = 0
            cnt += 1
            dvd += i

    # DVD 의 용량이 너무 작은 경우
    if cnt > m:
        lt = mid + 1
    # DVD 의 용량이 큰 경우
    else:
        rt = mid - 1
        # 지정된 DVD 갯수와 같고 최소용량이라면 결과 갱신
        if mid < res:
            res = mid

print(res)

# 수행시간 체크
# print('수행시간 : ', time.time() - start_time)
