'''
소수 구하기

M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다.
(1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
'''
import math


def solution(x):
    if x == 1:
        return False # 소수가 아님
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return False # 소수가아님
        return True # 소수임


a,b = map(int,input().split())


for i in range(a,b+1):
   ans = solution(i)
   if ans:
       print(i)