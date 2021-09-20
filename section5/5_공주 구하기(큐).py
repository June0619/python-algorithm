import sys
import time
import random as r
from collections import deque

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, k = map(int, input().split())

deq = deque()

# n명의 왕자를 큐에 대기시킴
for i in range(1, n+1):
    deq.append(i)

# 초기 카운트
cnt = 1
# 큐에 왕자가 한 명 남을 때까지 반복
while len(deq) > 1:
    # k 번째 왕자의 차례가 오지 않았다면
    if cnt != k:
        # bottom 에 있는 왕자를 큐의 rear 로 돌려보냄
        deq.append(deq.popleft())
        # 카운트 증가
        cnt += 1
    # k 번째 왕자의 차례가 왔다면
    else:
        # 큐에서 제거
        deq.popleft()
        # 카운트 초기화
        cnt = 1

# 한 명 남은 왕자의 번호를 출력
print(deq[0])


# 수행시간 체크
print('수행시간 : ', time.time() - start_time)