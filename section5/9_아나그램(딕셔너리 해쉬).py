import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

word1 = input()
word2 = input()

word1_dict = dict()
word2_dict = dict()

for w in word1:
    if w not in word1_dict.keys():
        word1_dict[w] = 1
    else:
        word1_dict[w] += 1

for w in word2:
    if w not in word2_dict.keys():
        word2_dict[w] = 1
    else:
        word2_dict[w] += 1

for key, val in word1_dict.items():
    if key in word2_dict.keys() and word2_dict[key] == val:
        continue
    else:
        print("NO")
        break
else:
    print("YES")
# 수행시간 체크
print('수행시간 : ', time.time() - start_time)