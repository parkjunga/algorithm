def solution(priorities, location):
    answer = 0
    p = priorities.copy() # 복사본 생성
    j = priorities.pop(0) # 0 번째를 일단 꺼낸다
    stack = []
    for i in range(len(priorities)):
        if j <= max(priorities): # 최대값이 있다면
            stack.append(max(priorities)) # 3 2
            priorities.pop(priorities.index(max(priorities)))
        else:
            stack.append(j)
            stack.append(priorities[0])
    print(stack)
    answer = stack.index(p[location]) + 1
    return answer


priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))