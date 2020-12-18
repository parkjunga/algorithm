'''
별 찍기 - 5 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	28044	15945	14389	57.540%
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제

별은 가운데를 기준으로 대칭이어야 한다.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

예제 입력 1
5
예제 출력 1
    *
   ***
  *****
 *******
*********
'''
from sys import stdin
n = int(stdin.readline())
for a in range(1, n+1):
    print(' ' * (n-a) + '*' * (2*a-1))


n = int(input())

for a in range(1, n+1):
    print(' ' * (n-a) + '*' * (2*a-1))