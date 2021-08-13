import sys
# sys.stdin = open('input.txt', 'rt')

# tc 입력
tc = int(input())

for idx in range(tc):

    # 문제에서 지정한 변수 입력
    n, s, e, k = map(int, input().split())

    # n개의 개수 입력받기
    numbers = list(map(int, input().split()))

    # s번째 수 부터 e번째 수 별도 저장
    selected_numbers = numbers[s-1:e]

    # 오름차순 정렬
    selected_numbers.sort()

    # k번째 수 출력
    # print('#'+str(idx+1), selected_numbers[k-1], sep=' ')
    print('#%d %d' % (idx + 1, selected_numbers[k - 1]))