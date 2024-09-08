def solution(num_list, n):
    answer = []
    a = num_list[n:]
    b = num_list[:n]
    answer = a + b
    return answer


num_list = [5, 2, 1, 7, 5]
n = 3

print(solution(num_list,n))