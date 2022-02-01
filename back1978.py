'''
소수찾기
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

'''

import math


def solution(x):
    if x == 1:
        return False # 소수가아님
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return False # 소수가아님
        return True



n = int(input())
arr = map(int,input().split())
arr = list(arr)
answer =  0
for i in range(len(arr)):
    if solution(arr[i]):
        answer += 1
print(answer)


