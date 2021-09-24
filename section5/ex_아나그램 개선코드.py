import sys
import time
import random as r

sys.stdin = open('input.txt', 'rt')
start_time = time.time()

word1 = input()
word2 = input()

string_hash = dict()

for w in word1:
    string_hash[w] = string_hash.get(w, 0) + 1

for w in word2:
    string_hash[w] = string_hash.get(w, 0) - 1

for i in word1:
    if string_hash.get(i) > 0:
        print("NO")
        break
else:
    print("YES")
# 수행시간 체크
print('수행시간 : ', time.time() - start_time)