'''
6097 : [기초-리스트] 설탕과자 뽑기
부모님과 함께 놀러간 영일이는
설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)

격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
'''
h,w = input().split()
arr = [[0 for _ in range(int(w)+1)] for _ in range(int(h)+1)]

n = int(input())
for i in range(n):
    l,d,x,y= input().split()
    for j in range(int(l)):

        nx = int(x) + j
        ny = int(y) + j
        #print("x =",x,"nx = ",nx, "y =", y, 'ny =',ny)

        if int(d) == 0:
            arr[int(x)][ny] = 1
#            arr[int(x)][ny] = 1
        else:
            arr[nx][int(y)] = 1
#            arr[ny][int(x)] = 1
   # print()
for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
        print(arr[i][j],end=' ')
    print()

'''
100 100
10
5 1 8 7
10 0 15 23
7 0 87 15
9 1 77 77
5 1 2 1
6 1 1 5
100 0 100 1
98 0 99 3
15 1 50 51
9 0 33 27
'''