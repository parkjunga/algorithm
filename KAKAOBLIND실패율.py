def solution(N, stages):
    answer = []
    tmp = {}
#    tmp = { i:0 for i in range(1,N+1) }
    # 전체스테이지 개수
    for i in range(1,N+1):
        tmp[i] = 0

    # 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stage
    for j in range(len(stages)):
        if stages[j] in tmp.keys():
            tmp[stages[j]] += 1

    length = len(stages)
    tmp2 = {}
    for t in tmp.items(): # 런타임에러발생 모두 0 인경우에 대한 예외처리가 안되었음
        if length == 0 :
            tmp2[t[0]] = 0
        else:
            tmp2[t[0]] = t[1] /length
            length = length - t[1]
    dic2 = sorted(tmp2.items(), key = lambda item : item[1],reverse=True)
    for i in range(len(dic2)):
        answer.append(dic2[i][0])


    return answer
N = 5
stages = [2,2,2,2,2]
print(solution(N,stages))