# 전역변수 지역변수
def DFS1():
    cnt = 3
    print(cnt)


def DFS2():
    global cnt # 이부분은 10라인에 로컬변수가 없이 에러나는것을 방지하기위해
    if cnt == 5:
        cnt = cnt + 1
        print(cnt)

cnt = 5
DFS1()
DFS2()
print(cnt)


def DFS():
    a = a + 4  # 이 경우 a라는 로컬변수를 선언하려고하는데 a라는 로컬변수를 찾게되고 그러나 찾을 수 없어 에러 발생
    print(a)

a = [1,2,3]
DFS()
print(a)