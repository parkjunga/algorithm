'''
오르막 수 분류

문제
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.
예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.
수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

입력
첫째 줄에 N (1 ≤ N ≤ 1,000)이 주어진다.

000 010
001 011
002 012
003 013
004 014
005 015
006 016
007 017
008 018
009 019
출력
첫째 줄에 길이가 N인 오르막 수의 개수를 10,007로 나눈 나머지를 출력한다.
이게 규칙
10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
00
01 11 22 33 44 55 66 77 88 99
02 12 23 34 45 56 67 78 89
03 13 24 35 46 57 68 79
04 14 25 36 47 58 69
05 15 26 37 48 59
06 16 27 38 49
07 17 28 39
08 18 29
09 19
예제 입력 1
1
예제 출력 1
10
예제 입력 2
2
예제 출력 2
55
예제 입력 3
3
예제 출력 3
220

무조건 뒤는 같거나 + 여야되는게 조건
1) n번째 자릿수의 자릿값 뒤에는 0-9까지 다 올 수있음.


동적계획법에 관한 문제였기 때문에 점화식이 필요했다.
처음에 점화식을 어떻게 구해야하는지 어려웠다.
어떤 문제인지는 알겠는데 이 규칙을 어떻게 식으로 표현하지? 라는 생각이 먼저 들었다.
그렇게 찾은 점화식은

i = 수의 길이 , j = 0~9의 숫자

j = 0	, dp[i][j] = dp[i-1][j+1]
j = 1-8	, dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
j = 9	, dp[i][j] = dp[i-1][j-1]
더 풀어서 설명해보면

수의 길이 N = 1 ,

0을 제외한 1~9 까지해서 9개의 계단 수가 만들어진다.

1 2 3 4 5 6 7 8 9

수의 길이 N = 2 ,

앞자리에 0이 올 수 없기 때문에 1부터 시작한다.

10 21 32 43 54 65 76 87 98
12 23 34 45 56 67 78 89 --

수의 길이 N=3 ,

101 121 210 232 321 343 432 454 543 565 654 676 765 787 876 898 987
--- 123 213 234 323 345 434 456 545 567 656 678 767 789 878 --- 989

수의 길이가 3 일 때부터 차례대로 살펴보니 어떠한 규칙으로 경우의 수가 증가하는지 알 수 있었다.

길이가 증가할 때, 앞자리 숫자가
0이면 뒤에 1이 오고
9이면 뒤에 8이 오고
1~8이면 뒤에 앞자리 수의 -1 또는 +1
가 온다는 것을 알 수 있었다.

따라서 조건문을 이용해 코드를 작성했다.


'''

# 이미 0으로 시작
# i = 수의 길이 , j = 0~9의 숫자

'''
앞자리에 0이 올 수 없기 때문에 1부터 시작한다.

10 21 32 43 54 65 76 87 98
12 23 34 45 56 67 78 89 --

00
01 11 22 33 44 55 66 77 88 99
02 12 23 34 45 56 67 78 89
03 13 24 35 46 57 68 79
04 14 25 36 47 58 69
05 15 26 37 48 59
06 16 27 38 49
07 17 28 39
08 18 29
09 19

new_nums = nums[i] + new_nums[i-1]
참고 > https://suri78.tistory.com/92

'''
from sys import stdin
n = int(stdin.readline())

nums = [1] * 10
for j in range(n-1):
    for i in range(1,10):
        nums[i] = (nums[i] + nums[i-1])

print(sum(nums) % 10007)