import math


def len(a, b):
  return (a * b) //  math.gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    m =  len(denom1,denom2)
    m1 = numer1 * (m//denom1)

    m2 = numer2 * (m//denom2)

    top = m1 + m2
    bottom = m

    g = math.gcd(top, bottom)

    answer = [top//g, bottom//g]
    return answer

print(solution(1,2,3,4))


