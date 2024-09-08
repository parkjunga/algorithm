def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            return answer
        else:
            answer = 0
    if answer == 0 :
        answer = -1
    return answer

num_list = [12, 4, 15, 46, 38, -2, 15]
print(solution(num_list))