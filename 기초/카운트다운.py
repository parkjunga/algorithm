def solution(start_num, end_num):
    answer = []
    for i in range(start_num,end_num-1,-1) :
        answer.append(i)
    return answer

start_num = 10
end_num = 3
print(solution(start_num,end_num))