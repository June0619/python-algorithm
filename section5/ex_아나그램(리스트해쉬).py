import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

word1 = input()
word2 = input()

word1_list = [0 for _ in range(58)]
word2_list = [0 for _ in range(58)]

for w1 in word1:
    word1_list[ord(w1)-65] += 1

for w2 in word2:
    word2_list[ord(w2)-65] += 1

for i in range(len(word1_list)):
    if word1_list[i] != word2_list[i]:
        print("NO")
        break
else:
    print("YES")

# 수행시간 체크
print('수행시간 : ', time.time() - start_time)