'''
수 정렬하기 분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	128 MB	66008	37163	25978	58.123%
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1
5
5
2
3
4
1

'''

from sys import stdin

n = int(stdin.readline())
arr = []
if 1 <= n <= 1000:
    for _ in range(n):
        arr.append(int(stdin.readline().strip()))      # 공백 제거
        arr.sort()

for i in range(len(arr)):
    print(arr[i])
