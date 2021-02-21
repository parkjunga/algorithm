'''
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가
여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려
고 합니다. 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력
하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값
은 22입니다.

'''

import sys

sys.stdin = open("input.txt","rt") # 파일이름, 파일모드(read)

N, K = map(int,sys.stdin.readline().split())

arr = list(sys.stdin.readline().split())
arr.sort(reverse=True)
sum = 0
tmp = []
# 리스트와 번호가 인덱스 차이가 있어 0번이 1번임으로 -1을해야 2 == 3 이다.
for i in range(N):
    if K-1 > i:
        sum += int(arr[i])
    else:
        tmp.append(arr[i])
#print(arr)
for j in range(len(tmp)):
    if j == K-1:
        sum += int(tmp[j])
print(sum)






































































































































































































































