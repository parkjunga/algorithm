def solution(my_string, is_suffix):
    answer = 0
    if my_string.endswith(is_suffix):
        answer = 1
    return answer


my_string = "banana"
is_suffix = "ana"

print(solution(my_string,is_suffix))