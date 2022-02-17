def solution(land):
    answer = 0
    list = []
    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j] == max(land[i]) and j not in list:
                list.append(j)
                answer += land[i][j]
                if i+1 < len(land):
                    land[i+1][j] = 0
    return answer

land = [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]
answer =  solution(land)
print(answer)