def solution(my_string, n):
    answer = my_string[len(my_string)-n:]
    return answer

my_string = "ProgrammerS123"
n = 11
print(solution(my_string,n))