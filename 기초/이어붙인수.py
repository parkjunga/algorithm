def solution(num_list):
    answer = 0
    odd_str = ''
    add_str = ''
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            odd_str += str(num_list[i])
        else:
            add_str += str(num_list[i])

    answer = int(odd_str) + int(add_str)
    return answer


num_list = [3, 4, 5, 2, 1]
print(solution(num_list))