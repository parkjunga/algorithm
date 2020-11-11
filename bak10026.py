'''
적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다.
또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1)
하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

출력
적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

예제 입력 1
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
예제 출력 1
4 3
'''
from collections import deque
from sys import stdin
n = int(stdin.readline()) # 입력값
listEx = [stdin.readline().split() for _ in range(n)] # n은 사용자 임의  std.readine().split() 에 대해서 n번 박
# 문자열 한개ㅇ에 접근하려면 print(listEx[0][0][4])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count1 = 0
count2 = 0 # 적록색약
visit = [[0]*n for _ in range(n)]

def bfs(v1,v2):
    queue = deque()
    queue.appendleft([v1,v2])
    visit[v1][v2] = 1 # 방문했으니 1ㅗ
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx and nx < n and 0 < ny and ny < n:
                if listEx[nx][0][ny] == listEx[x][0][y] and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    queue.appendleft([nx,ny])


for i in range(len(listEx)):
    for j in range(len(listEx[i][0])):
        #print(listEx[i][0][j]) # 인덱스 한개한개 출력
        #print(listEx[i][0])
        if visit[i][j] == 0:
            count1 += 1
            bfs(i,j)

for i in range(len(listEx)):
    for j in range(len(listEx[i][0])):
        print(type(listEx[i][0][j]))
        if listEx[i][0][j] == 'R':
            listEx[i][0][j]

for i in range(len(listEx)):
    for j in range(len(listEx[i][0])):
        #print(listEx[i][0][j]) # 인덱스 한개한개 출력
        #print(listEx[i][0])
        if visit[i][j] == 0:
            count2 += 1
            bfs(i,j)

print(count1,count2)