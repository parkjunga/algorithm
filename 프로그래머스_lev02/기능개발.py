import math

def solution(progresses, speeds):
    answer = []
    tmp = []
    for i in range(len(progresses)):
        a = 100 - progresses[i]
        a = math.ceil(a/speeds[i])
        if len(tmp) == 0:
            tmp.append(a)
            answer.append(1)
        else:
            if tmp[-1] < a:
                tmp.append(a)
                answer.append(1)
            else:
                answer[-1] += 1
    return answer

progresses = [70, 90, 99, 99, 80, 99] # 1, 3,2
speeds =  [50, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))