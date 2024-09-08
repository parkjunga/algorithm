def solution(num, n):
    answer = 0
    if num % n == 0:
        answer = 1
    return answer

num = 98
n = 2
print(solution(num,n))