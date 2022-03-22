a,b,c = map(int,input().split())
# c * n = a + ( b * n )
if b >= c :
    print(-1)
else:
    n = a // (c - b) + 1
    print(n)
