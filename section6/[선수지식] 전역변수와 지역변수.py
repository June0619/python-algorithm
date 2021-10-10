""" 전역변수와 지역변수 """


def dfs1():
    # cnt 라는 이름의 지역변수를 할당하고 3을 할당함
    cnt = 3
    print(cnt)


def dfs2():
    # error -> dfs2 함수 내에서 지역변수 cnt 를 새로 할당했기 때문에 if 문 내부에서 참조할 변수를 못찾음
    # if cnt == 5:
    #     cnt = cnt + 1
    #     print(cnt)
    global cnt
    if cnt == 5:
        cnt = cnt + 1
        print(cnt)


def dfs3():
    # 아래 예시는 변수를 할당하는 것과 달리, 리스트 내 특정 인덱스의 주소를 참조하는 개념이기 때문에 에러 발생하지 않음
    a[0] = 7
    print(a)


def dfs4():
    # 2번 예시와 같이 지역 변수 b에 새로운 리스트를 할당함
    b = [1, 2]
    print(b)


if __name__ == "__main__":
    cnt = 5
    dfs1()
    dfs2()
    print(cnt)

    a = [1, 2, 3]
    dfs3()
    print(a)

    b = [1, 2, 3]
    dfs4()
    print(b)
