'''
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.


nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

'''


def solution(nums):
    answer = 0
    list = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for t in range(j+1, len(nums)):
                sum = nums[i] + nums[j] +nums[t]
                # 중복된 합을 제거할 필요 없다!
                list.append(sum)

    for s in range(len(list)):
        ans = 에스트라체(list[s])
        if ans == 1:
            answer += 1
    return answer


def 에스트라체(m):
    count = 0
    for i in range(2,m+1):
        if m % i == 0:
            count += 1

    return count











# def solution(nums):
#     answer = -1
#     count = 0
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             for t in range(j+1, len(nums)):
#                 nums[i]
#
#     return answer
#
# def test(num1,nums2,num3):
#     sum = num1+nums2+num3
#     list = [False, False] + [True] * (sum - 1)
#     primes = []
#
#     for i in range(2, sum+1): # 2 ~ n 까지 출력
#         if list[i]: # 2 부터 n 까지 일단은 true일때
#             primes.append(i) # primes배열에 추가
#             for j in range(2*i,sum+1,i): # 이후 2의배수,3의배수 등등 으로 n사이의 값으로 볼때 그 값에 대해서는 False로 바꿈
#                 list[j] = False
#     answer = len(primes)
#     print(primes)

nums = [1,2, 3, 4, 5, 7 , 8]
ans = solution(nums)
print(ans)