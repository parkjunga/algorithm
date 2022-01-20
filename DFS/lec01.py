# 재귀함수는 반복문의 대체재
# 재귀함수와 스택을 생각
# 재귀함수는 스택을 이용해서 사용된다.
def DFS(x):
    if x > 0:
        DFS(x-1)
        print(x, end=' ')

x = int(input())
DFS(x)