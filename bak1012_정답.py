import sys
sys.setrecursionlimit(10000)

'''
1. 현재 위치에서 상하좌우 확인한다.

2. 행렬 범위를 넘지 않고 조건을 만족한다면 지나온 값을 -1로 바꾸고 계속 연결된 지점을 탐색해 나간다.

3. 탐색을 마치면 카운트 값을 1 올려주고, 다른 요소들을 탐색한다.

4. 모든 연결된 부분들을 탐색을 마치면, 부분들이 몇 개인지 출력한다.

 
'''
def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    # 상,하,좌,우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx,ny)

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    matrix = [[0] * m for _ in range(n)]
    cnt = 0

    # 행렬 생성
    for _ in range(k):
        m, n = map(int,input().split())
        matrix[n][m] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0:
                dfs(i,j)
                cnt += 1
    print(cnt)

