import itertools
import math


# 소수 판별
def is_prime_num(n):
    answer = True
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            answer = False
    return answer


def solution(n):
    count = 0
    n_list = list(n)
    arr = []

    # 나올수 있는 순열 담기
    for i in range(1, len(n_list) + 1):
        # i로 한 이유는 여러개를 받기위해
        combination = itertools.permutations(n_list, i)
        # 순열을 리스트화
        com = list(combination)
        for i in range(len(com)):
            # 모든 조합에서 0과 1을 제외하고 리스트에 담음
            if int(''.join(list(com[i]))) > 1:
                # 튜플을 리스트 > 문자열 > 숫자로
                arr.append(int(''.join(list(com[i]))))
    # 중복 제거를 위해 set
    arr = set(arr)
    # 다시 리스트화
    arr = list(arr)
    for i in range(len(arr)):
        if is_prime_num(arr[i]):
            count += 1
    return count
