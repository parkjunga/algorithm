# 이진트리순회

# 전위순회
def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=" ") # 방문, 호출전에 본연의 작업을하는것을 전위순회
        DFS(v*2)
        DFS(v*2+1)


DFS(1)
print(' --- ')
# 중위순회
def DFS2(v):
    if v > 7:
        return
    else:
        DFS(v*2) # 왼쪽 자식 먼저 처리리        print(v, end=" ")  # 방문, 호출전에 본연의 작업을하는것을 전위순회
        print(v,end= ' ')
        DFS(v*2+1)

print(' --- ')
# 후위순회, 대표적인 처리방법 병합정렬
def DFS3(v):
    if v > 7:
        return
    else:
        DFS(v*2) # 왼쪽 자식 먼저 처리리        print(v, end=" ")  # 방문, 호출전에 본연의 작업을하는것을 전위순회
        DFS(v*2+1)
        print(v,end=' ')
DFS3(1)
