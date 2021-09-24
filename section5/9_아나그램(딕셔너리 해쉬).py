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
    # dictionary 자료형에서 해당 key 에 해당하는 공간이 null 일 경우 기본 값 지정
    word1_dict[w] = word1_dict.get(w, 0) + 1
    # if w not in word1_dict.keys():
    #     word1_dict[w] = 1
    # else:
    #     word1_dict[w] += 1

for w in word2:
    word2_dict[w] = word2_dict.get(w, 0) + 1
    # if w not in word2_dict.keys():
    #     word2_dict[w] = 1
    # else:
    #     word2_dict[w] += 1

for key, val in word1_dict.items():
    # if key in word2_dict.keys() and word2_dict[key] == val:
    # 위 스타일을 적용하여 더 간결하게 표현
    if word2_dict.get(key, 0) == val:
        continue
    else:
        print("NO")
        break
else:
    print("YES")
# 수행시간 체크
print('수행시간 : ', time.time() - start_time)