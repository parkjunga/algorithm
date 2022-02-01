'''
소수판별
* 소수는 1보다 큰 자연수중에서 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수이다.
Ex 6은 1,2,3,6 으로 나뉘어지므로 소수가 아님
   7은 1과 7을 제외하고는 나누어 떨어지지않으므로 소수이다.
'''

def is_prime_number(x):
    # 2부터 x -1 까지 모두 확인해서
    for i in range(2,x):
        # x가 해당수로 나누어진다면
        if x % i == 0:
            return False # x 아님
        return True # 소수임

'''
위에는 2부터 x - 1 까지 모든 자연수 연산수행해야됨 
모든 수를 하나씩 확인한다는 점에서 시간 복잡도가 O(x)

약수의 성질
모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이루는 것을 알 수 있다.
'''

# 개선된 알고리즘

import math


def is_prime_number2(x):

    # 2부터 x의 제곱근까지의 모든 수를 확인하여
    for i in range(2,int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가아님
    return True # 소수임


print(is_prime_number2(13))


def prime_list(x):
    all_prime = [True] * x

    m = int(x ** 0.5) # 약수 구하기
    for i in range(2, m + 1):
        if all_prime[i]:
            for j in range(i+j, x, i): # i이후의 i배수들은 False
                all_prime[j] = True
    return [i for i in range(2, x) if all_prime[i] == True]
