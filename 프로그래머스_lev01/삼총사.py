import itertools


def solution(number):
    answer = 0
    arr = list(itertools.combinations(number, 3))
    for i in range(len(arr)):
        if sum(list(arr[i])) == 0:
            answer += 1

    return answer


numbers = [-3, -2, -1, 0, 1, 2, 3]
print(solution(numbers))