def solution(n, lost, reserve):
    answer = 0
    # 겹치지 않는 경우
    for i in range(1,n+1):
        if i not in lost and i not in reserve:
            answer +=  1


    return answer
n = 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n,lost,reserve))