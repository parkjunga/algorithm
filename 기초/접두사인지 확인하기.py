def solution(my_string, is_prefix):
    answer = 0
    if my_string.startswith(is_prefix):
        answer = 1
    return answer

#my_string = "banana"
#is_prefix = "ban"
#print(solution(my_string,is_prefix))