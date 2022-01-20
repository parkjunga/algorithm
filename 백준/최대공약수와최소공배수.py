def solution2(a,b):
    n = solution3(a,b)
    ans = n * a//n * b//n
    return ans

def solution3(a,b):
    if b == 0:
        return a
    else:
        return solution3(b,a%b)
#print(solution3(24,18))


def solution(a,b):
    if a > b:
        tmp = a
        a = b
        b = tmp

    while b != 0:
        n = a % b
        a = b
        b = n

    return a

a,b = map(int,input().split())
print(solution3(a,b))
print(solution2(a,b))