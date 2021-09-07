import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

# 그냥 sort 함수를 사용하면 튜플 가장 맨 앞 인덱스 값에 의해서 정렬된다.
meeting.sort(key=lambda x: (x[1], x[0]))

# 회의가 끝나는 시간을 잘 기록해야 함
end_time = 0
cnt = 0

for s, e in meeting:
    if s >= end_time:
        end_time = e
        cnt += 1

print(cnt)

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)