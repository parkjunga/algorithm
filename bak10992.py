'''
별 찍기 - 17 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	9438	6363	5858	68.812%
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

예제 입력 1
1
예제 출력 1
*
예제 입력 2
2
예제 출력 2
1*1
***
예제 입력 3
3
예제 출력 3
12*12
1* *
*****
1 2 5
예제 입력 4
4
예제 출력 4
   *
  * *
 *   *
*******
    *
  *123*
 *12345*
*********
'''
from sys import stdin

n = int(stdin.readline())
# for i in range(n,0,-1):
#     print(i*'1'+'*'*i+i*'1')
# n = int(input())

for a in range(1, n+1):
    if a == 1 or a == n:
        print(' ' * (n-a), '*' * (2*a-1), sep='')
    else:
        print(' ' * (n-a), '*', ' ' * ((a-1) * 2 -1), '*', sep='')