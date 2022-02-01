'''
소수

베르트랑 공준

베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

입력의 마지막에는 0이 주어진다.
'''

import math
import sys


def solution(x):
    if x == 1 :
        return False # 소수가 아님
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x % i == 0:
                return False # 소수가아님
        else:
            return True


all_list = list(range(123456*2)) # 문제의 주어진 범위
save_list = []

for i in all_list:
    if solution(i): # 소수 판별된 값은
        save_list.append(i) # 배열에 담아준다


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        answer = 0
        for value in save_list:
            if n < value <= n * 2: # 범위제한
                answer += 1
        print(answer)
