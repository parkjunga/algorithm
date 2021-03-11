from collections import Counter

N = int(input())
lst = sorted(list(map(int, input().split()))) # 정렬
M = int(input())
card = list(map(int, input().split()))
dic = {}

for n in lst:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
#print(' '.join(str(dic[c]) if c in dic else '0' for c in card ))
for c in card:
    if c in dic:
        pass
    else:
        dic[c] = 0
    print(' '.join(str(dic[c])),end=' ')