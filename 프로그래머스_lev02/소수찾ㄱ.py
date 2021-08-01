import math
from itertools import permutations
def solution(numbers):
    answer = 0
    tmp_list = []
    for i in range(len(numbers)):
        if numbers[i] != '1' and numbers[i] != '0':
            tmp_list.append(numbers[i])
    # 순열 조합을 이용한다.
    n_list = list(permutations(list(numbers),len(list(numbers))))
    n_list = n_list + tmp_list
    for i in range(len(n_list)):
        n_list[i] = ''.join(list(n_list[i]))
    new_list = list(set(n_list))

    # 가공
    for i in range(len(new_list)):
        if new_list[i][0] == '0':
            new_list[i] = new_list[i][1:]
    # 마지막
    sosu = 0
    for j in range(len(new_list)):
        sosu = 0
        new_list[j] = int(new_list[j])
        if new_list[j] == 2 or new_list[j] == 3: answer += 1
        if new_list[j] >= 4 :
            for i in range(2,new_list[j]):
                if new_list[j] % i == 0:
                    sosu = 1
                    break
            if sosu != 1:
                answer += 1
    return answer
# def sosu(num):
#     arr = [True for i in range(num+1)]
#
#     for i in range(2, int(math.sqrt(num)) + 1): # 2부터 제곱근까지 모든 수를 확인해
#         if arr[i] == True: # i 제외 모든 i배수 지운다
#             j = 2
#             while i * j <= num:
#                 arr[i*j] = False
#                 j += 1
#     return [i for i in range(2,num+1) if arr[i]]

numbers = '1231'
print(solution(numbers))

# 1과 자기자신만 남은게 소수
'''
1. 숫자로 만들수 있는 숫자를 배열에 저장한다 
2. 이 숫자가 소수인지 판별한다,
'''