def solution(dirs):
    command = {'U': (0,1), "D":(0,-1), "L":(-1,0), "R":(1,0)} # 좌표값
    road = set()
    cur_x, cur_y = (0,0)  # 기본 셋팅값
    for d in dirs:
        next_x, next_y = cur_x + command[d][0], cur_y + command[d][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5:
            road.add((cur_x, cur_y, next_x, next_y)) # 출발지점x, 출발지점y, 도착지점x, 도착지점y
            road.add((next_x, next_y, cur_x, cur_y)) # 도착지점x, 도착지점y, 출발지점x, 출발지점y
            # 출발지점과 도착지점이 반대여도 같은 간선을 쓰기 때문에 한번 저장할때 둘 다 저장한다!!!!
            cur_x, cur_y = next_x, next_y # 출발지점을 0으로 시작하지않고 도착한 지점으로 다시 출발지 설정
    return len(road) // 2

dirs = "ULURRDLLU"
paths = solution(dirs)
print(paths)