'''
# 이진탐색으로 풀면 안됨 이유는 단일 target인경우는 이진탐색이 효과적이지만 target이 여러개니까 해시로 해놓고
 탐색이아닌 key value가 더 승산있음.

Q. 숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.


'''

from sys import stdin

N = int(stdin.readline()) # 상근이가 가지고 있는 숫자 카드의 갯수
arr1 =list(map(int,stdin.readline().split())) # 숫자카드안의 있는 정수
M =int(stdin.readline())
arr2 = list(map(int,stdin.readline().split()))
arr3 = [0] * M
cnt = 0
'''
1. 처음에 한개씩 비교해야될꺼같아서 for문을 돌린다.
M 리스트크기안에 N 리스트를 돌리고 M숫자한개랑 N리스트숫자들중 있는것을 비교해서 카운트후 
다시 M을 돌릴때 카운트 숫자만큼 arr3에 넣고 다시 리셋 반복
'''

for i in range(M):
    arr3[i] = cnt
    cnt = 0
    for j in range(N):
        if arr2[i] == arr1[j]:
            cnt += 1
            #print(arr2[i], arr1[j],cnt)

print(arr3)