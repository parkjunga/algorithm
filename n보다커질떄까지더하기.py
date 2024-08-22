def solution(numbers, n):
    answer = 0
    for i in range(len(numbers)):
        answer += numbers[i]
        if answer > n :
            return answer
    return answer

numbers = [34, 5, 71, 29, 100, 34]
s = solution(numbers, 123)
print(s)