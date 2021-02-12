'''
# 큐 2 아니고 이진탐색으로 풀어야됨.

Q. 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.


'''

from sys import stdin



from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

#print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))

for i in M:
    print(hashmap)
    print("아이값 확인 =>",i, "디엔드")
    try:
        print(hashmap[i], end = " ")
    except:
        print(0, end=" ")