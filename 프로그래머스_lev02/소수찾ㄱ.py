from itertools import permutations
def solution(numbers):
    answer = 0

    if numbers == '1':
        return answer

    if numbers == '2' or numbers == '3':
        return 1

    # 조합
    numbers = list(numbers)
    arr2 = []

    # 기본적으로 값 넣기
    for i in range(len(numbers)):
        if int(numbers[i]) > 1:
            arr2.append(int(numbers[i]))
    for j in permutations(numbers,len(numbers)):
        j = int(''.join(j))
        arr2.append(j)
    arr2 = set(arr2)
    arr2 = list(arr2)

    arr2 = sorted(arr2)
    for i in range(len(arr2)):
        ans = test(arr2[i])
        if ans != '소수아님':
            answer += 1
    return answer

def test(num):
    answer = '';
    for i in range(2,(num//2)+1):
        if num%i == 0:
            answer = '소수아님'
    return answer
numbers = '1231'
print(solution(numbers))

# 1과 자기자신만 남은게 소수
'''
1. 숫자로 만들수 있는 숫자를 배열에 저장한다 
2. 이 숫자가 소수인지 판별한다,
'''