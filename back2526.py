'''
오븐시계 if
'''

a,b = map(int,input().split())
c = int(input())

if b + c < 60:
    print(a, b+c)
else:
    while True:
        if b + c < 120:
            a = a + 1
            b = b + c - 60
            break
