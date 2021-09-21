import sys
import time
import random as r
from collections import deque

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

# 필수과목 순서
input_str = input()
# 테스트 케이스
tc = int(input())
cnt = 1

while cnt <= tc:

    deq = deque(input_str)
    timestamp = input()

    for i in timestamp:
        # 큐에 자료가 남아 있고, 필수과목에 해당하고, 필수과목 순서와 일치하는 경우
        if deq and i in deq and i == deq[0]:
            deq.popleft()
        # 필수과목에 해당하지만 순서가 틀린 경우
        elif deq and i in deq and i != deq[0]:
            break

    if deq:
        print('#{} NO'.format(cnt))
    else:
        print('#{} YES'.format(cnt))

    cnt += 1

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)
