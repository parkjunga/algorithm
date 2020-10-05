# 각 노드가 연결된 정보를 표현 (2차원 리스트), 일반적으로 리스트의 인덱스가 1번부터인경우가 많아 0번쨰는 비워둠
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트) 8번노드까지 가지고있지만 인덱스 0은 사용하지 않으니까 9개 만듦
visited = [False] * 9

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)