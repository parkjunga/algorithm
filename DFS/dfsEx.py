N,M,V = map(int,input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited1 = [False] * (N+1)
visited2 = visited1.copy()

for _ in range(M): # M은 간선
    x,y = map(int,input().split())
    graph[x][y] = 1 # 양방향이니깎
    graph[y][x] = 1 # 양방향이니까


def dfs(V):
    visited1[V] = True # 방문한걸로 친다
    print(V, end=' ')
    for i in range(1,N+1): # 그래프 접점1부터 4까지
        if graph[V][i] == 1 and visited1[i] == False:
            dfs(i)


def bfs(V):
    visited2[V] = True # 방문한걸로 친다
    queue = [V]
    while queue:
        v = queue.pop(0) # 선입선출
        print(v,end=" ")
        for i in range(1,N+1):
            if visited2[i] == False and graph[V][i] == 1:
                queue.append(i)
                visited2[i] = True



dfs(V)
print()
bfs(V)