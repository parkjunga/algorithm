def solution(arr):
    answer = 0
    return answer

def gcd(a,b):

    if a < b:
        tmp = a # b가 크면 a를 tmp에
        a = b # a 에 b를
        b = tmp # b에 tmp를

    while b != 0:
        n = a % b
        a = b
        b = n
    return a

print(gcd(3,4))

arr = [3,4,9,16]
#test
print(solution(arr))