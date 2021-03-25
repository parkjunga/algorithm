'''
# 문자열 반복

4차례 틀렸다.
대단한 이유가 있는줄 알았는데 알고보니
print() 줄넘김처리를 하지 않아 틀렸다.

'''
from sys import stdin
t = int(stdin.readline())
for i in range(t):
    r,s = map(str,stdin.readline().split())
    for j in s:
        print(int(r) * j, end='')
    print()