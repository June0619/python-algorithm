import sys
import time

sys.stdin = open('input.txt', 'rt')
start_time = time.time()


# 재귀함수와 스택
def DFS(x):
    if x > 0:
        print(x, end=' ')  # 3 2 1
        DFS(x - 1)
        print(x, end=' ')  # 1 2 3

# 1. 재귀함수를 호출하면 스택 메모리에 하나씩 함수의 호출 주소가 쌓인다.
# 2. 재귀함수가 호출되어 지역변수, 복귀 함수 메모리 등을 가지는 스택이 쌓이면 스택 프레임이라고 부름


if __name__ == "__main__":
    n = int(input())
    DFS(n)
