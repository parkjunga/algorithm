# 10진수 N이 입력되면 2집수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용해서 출력해야 합니다.
# 2 11
# 2  5 .. 1
# 2  2 .. 1
# 2  1 .. 0

def DFS(x):
    if x//2 > 0:
        n = x % 2
        DFS(x//2)
        print(n, end = '')
    else:
        print(x % 2, end = '')


def DFS_(x):
    if x == 0:
        return
    else:
        DFS_(x//2)
        print(x % 2, end='')
n = int(input())
DFS(n)