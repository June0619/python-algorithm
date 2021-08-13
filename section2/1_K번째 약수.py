import sys
# sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())

answer = 0
for idx in range(1, n+1):
    if n % idx == 0:
        k = k-1
    if k == 0:
        answer = idx
        break
else:
    answer = -1

print(answer)