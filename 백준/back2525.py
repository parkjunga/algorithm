'''
오븐시계
'''

a, b = map(int,input().split())
c = int(input())

n = b + c
'''
25 30
45

26 15

02 15
'''
# 60분이 넘어간다면
if n % 60 == 0:
    min = n // 60
    a = a + min
    b = n % 60
else: # 60분이 넘어가지 않는다면
    s = n % 60
    min = n // 60
    b = s

if a + min >= 24:
    a = a+min-24
print(a,b)