def solution(numbers):
    answer = 0

    basic = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(basic)):
        if i not in numbers:
            answer += i

    return answer

numbers = [1,2,3,4,6,7,8,0]
solution(numbers)