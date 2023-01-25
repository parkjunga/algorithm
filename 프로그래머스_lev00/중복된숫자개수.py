def solution(array, n):
    answer = 0
    for i in range(len(array)):
        answer = array.count(n)
    return answer