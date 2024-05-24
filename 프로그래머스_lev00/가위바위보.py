def solution(rsp):
    answer = ''
    ## 가위 2 < 바위 0
    ## 보 5 < 가위 2
    ## 바위 0  < 보 5
    tmp = {2:0,5:2,0:5}
    list = []
    for i in str(rsp):
        i = int(i)
        list.append(str(tmp[i]))
    answer = "".join(list)
    return answer

rsp = 205
answer = solution(rsp)
print(answer)