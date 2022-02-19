def solution(n):
    answer = 0
    tmp = 0
    count = 1
    for i in range(2,n):
        if count == 1 and n%i == 1:
            tmp = i
            count = 2
        elif n%i == 1 and tmp > i:
            tmp = i
    answer = tmp
    return answer


n = 12
result = solution(n)
print(result)