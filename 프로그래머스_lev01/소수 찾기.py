'''
소수 찾기
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3
'''
def solution(n):
    answer = 0
    # 0, 1 =False, 이후부터 다 True
    list = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n+1): # 2 ~ n 까지 출력
        if list[i]: # 2 부터 n 까지 일단은 true일때
            primes.append(i) # primes배열에 추가
            for j in range(2*i,n+1,i): # 이후 2의배수,3의배수 등등 으로 n사이의 값으로 볼때 그 값에 대해서는 False로 바꿈 
                list[j] = False
    answer = len(primes)
    return answer

# def solution(n):
#     answer = 0
#     for i in range(1,n+1): #  1%3
#         count = 0
#         if i % n == 0:
#             count += 1
#         for j in range(2,n): # 2,3,4,..
#             if i%j == 0:
#                 count += 1
#         if count == 1:
#             answer += 1
#     return answer


print(solution(n=10))

'''
1. 1 ~ n 사이의 숫자중 1과 자기자신외에 더 나눠지는게 알아보기 위해서는
2. 2 ~ n까지 사이중 자기자신외에 나눠지는게 있는지를 확인해본다 이래서 이중 for문 사용 
'''