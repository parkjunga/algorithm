def solution(N, stages):
    answer = []
    tmp = {}
    for i in range(1,N+1):
        tmp[i] = 0;

    for j in range(len(stages)):
        if stages[j] in tmp.keys():
            tmp[stages[j]] += 1
    length = len(stages)
    tmp2 = {}
    print(tmp)
    for t in tmp.items():
        tmp2[t[0]] = t[1] /length
        length = length - t[1]
    dic2 = sorted(tmp2.items(), key = lambda item : item[1],reverse=True)
    for i in range(len(dic2)):
        answer.append(dic2[i][0])


    return answer
N = 4
1,2,3,4,5
stages = [4,4,4,4,4]
print(solution(N,stages))