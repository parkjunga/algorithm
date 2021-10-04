def solution(arr):
    answer = 1
    for i in range(len(arr)):
        if i+1 < len(arr):
            print(arr[i],arr[i+1])
            print(gcd(arr[i],arr[i+1]))
    return answer

def gcd(a,b):
    tmp = 1
    b = 0
    print(a,b)
    while tmp > 0:
        if a%b != 0:
            a = b
            b = a%b
            tmp = a
            print(a,b,tmp)
        else:
            break
    return b


arr = [24,18]
solution(arr)