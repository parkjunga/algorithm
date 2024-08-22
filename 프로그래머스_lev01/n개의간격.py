def solution(num_list, n):
    answer = []
    for i in range(len(num_list)):
        if i % n == 0 :
            answer.append(num_list[i])
    return answer


num_list = [4, 2, 6, 1, 7, 6]
print(solution(num_list, 2))
