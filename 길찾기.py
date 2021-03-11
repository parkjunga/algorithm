# 길 중 처음 걸어본 길의 길이 구하기, 중복제거
def solution(dirs):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    d = {"U":0, "L": 1, "D":2, "R":3}
    visisted = set()
    answer = 0
    x, y = 0,0
    for dir in dirs:
        i = d[dir]
        print(i)
        nx, ny = x + dx[i], y + dy[i]
        print(nx, ny)
        if nx < -5 and nx > 5 and ny < -5 and ny > 5 : continue
        if (x, y, nx, ny) not in visisted: # 방문한적없을때
            visisted.add((x,y,nx,ny))
            visisted.add((nx,ny,x,y)) # 양방향
            answer += 1
            print((x,y,nx,ny),(nx,ny,x,y))
        x, y = nx, ny
    return answer



dirs = "ULURRDLLU"
paths = solution(dirs)
print(paths)