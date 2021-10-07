""" 전역변수와 지역변수 """


def dfs1():
    print(cnt)


def dfs2():
    if cnt == 5:
        print(cnt)


if __name__ == "__main__":
    cnt = 5
    dfs1()
    dfs2()
    print(cnt)
