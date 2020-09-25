# dangi = int(input())
# arr = [[0 for i in range(dangi+1)] for j in range(dangi + 1)]
# '''
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
# '''
#
# for i in range(dangi):
#     t = input().split()
#     print(t)
#     for j in range(dangi):
#         arr[i][j] = int(t)
#
# void dfs(int a, int b, int c) {
#     A[a][b] = c;
#     if( safe(a+1, b) && A[a+1][b] == 1 )
#     dfs(a+1, b, c);
#     if( safe(a-1, b) && A[a-1][b] == 1 )
#     dfs(a-1, b, c);
#     if( safe(a, b+1) && A[a][b+1] == 1 )
#     dfs(a, b+1, c);
#     if( safe(a, b-1) && A[a][b-1] == 1 )
# dfs(a, b-1, c); }
#
# 출처: https://12bme.tistory.com/122 [길은 가면, 뒤에 있다.]

from sys import stdin
n = int(input())
# 데이터 저장용 공간 matrix
matrix = [[0]*n for _ in range(n)]
# 방문 내역 저장용 visited
visited = [[0]*n for _ in range(n)]

# matrix에 아파트 유무 0과 1 저장
for i in range(n):
    line = stdin.readline().strip() # input() 과 똑같은거같음
    for j, b in enumerate(line):
        matrix[i][j] = int(b)

# 방향 확인용 좌표 dx와 dy
# 중앙을 기준으로 좌/우/위/아래
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# DFS 함수 정의
def dfs(x, y, c):
    visited[x][y] = 1   # 방문 여부 표시
    global nums            # 아파트 단지 수를 세기위한 변수
    # 아파트가 있으면 숫자를 세어줍니다.
    if matrix[x][y] == 1:
        #matrix[x][y] = c # 아파트 단지별 숫자 표시용
        nums += 1
    # 해당 위치에서 좌/우/위/아래 방향의 좌표를 확인해서 dfs 적용
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                dfs(nx,ny, c)

cnt = 1 # 아파트 단지 세기 위한
numlist = [] # 아파트 단지별 숫자
nums=0 # 아파트 수
for a in range(n):
    for b in range(n):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a,b,cnt)
            numlist.append(nums)
            nums = 0
#            cnt += 1 # 아파트 단지 별 표시용

print(len(numlist))
for n in sorted(numlist):
    print(n)