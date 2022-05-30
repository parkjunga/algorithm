def solution(a,b,c):
    sum = a*b*c
    sum = str(sum)
    arr = [0] * 10
    for i in str(sum):
        i = int(i)
        arr[i] += 1
    print(*arr,sep='\n')


a = int(input())
b = int(input())
c = int(input())

solution(a,b,c)