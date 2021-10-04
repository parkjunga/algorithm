def solution(arr):
    answer = 1
    tmp = arr[0]
    for i in range(1,len(arr)):
        tmp = gcd(tmp,arr[i])
        print(tmp)
    return answer

def gcd(a,b):
    while b > 0:
        tmp = b
        b = a % b
        a = tmp
    return a


arr = [9, 12, 15]
#test
print(solution(arr))