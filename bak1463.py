'''
1로 만들기 분류

문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

예제 입력 1
2
예제 출력 1
1
예제 입력 2
10
예제 출력 2
3
// 이해를 위한
N = 10 > 9 > 3 > 1 출력 3
N = 4 > 3 > 1 출력 2
N = 8 > 4 > 1 출력 3
# 최종적으로 틀렸으나 참고 받은 사이트 -> https://jobc.tistory.com/151
#############################################################################



우선 문제를 풀기 전에 어떤 알고리즘을 활용해서 풀어야할지부터 생각해야한다.

여기서는 연산을 활용한 최소값을 묻고있다.



예를 들어 10의 최소값을 구하려면 첫 단계로 연산 두 가지가 가능하다.

2로 나눠본다.

1을 빼본다.

만약 2번을 선택해서 1을 뺀다면 9가 되고 9에서의 최소 연산값을 구해야한다. 그런데 여기서 9의 최소 연산 개수를

구하려고 해도 경우의 수가 1을 빼거나 3으로 나누는 2가지 경우의 수가 생긴다.



만약 9의 최소 연산 횟수를 알고있다면 ?

1을 빼는 연산횟수 + 9의 최소 연산 횟수 = 10의 최소 연산횟수 가 된다.



그렇다면 9의 최소 연산 횟수는 어떻게 알고있을까?

9도 마찬가지로 전 단계의 최소 연산횟수가 필요하다.



그렇게 계속 거슬러 올라가다보면 결국 2와 3에서 시작되는 것을 알 수 있다. 이렇게 작은 해답에서 점점 큰 해답을

구할 때 쓰는 것이 동적프로그래밍이다.



※ 동적프로그래밍이 쓰이는 문제들은 대부분 이렇게 각 단계마다의 여러 경우의 수가 존재하고

그중에 최소값이나 최대값을 저장하고 있어야할 경우 동적프로그래밍이 쓰이는 것 같다.



동적 프로그래밍(Dynamic Programming)을 이용하여 문제 풀기

이제 어떤 알고리즘을 사용하여 풀어야하는지 파악했으니, 본격적으로 문제를 풀어보자.

우선 각 단계의 최소 연산 개수를 저장할 리스트를 생성한다.

각 단계마다 일어날 수 있는 경우의 수를 계산해서 그 중 가장 작은 연산 값을 저장한다.



동적프로그래밍을 이용하여 푸는 것을 눈치채더라도, 2번의 경우의 수를 모두 알아내 점화식을 세우는 것이 어렵다.

하지만 이 문제는 점화식을 세우는 것이 간단한 편이다.

각 단계마다 일어날 수 있는 경우의 수는 총 3가지이다. 이 3가지 중 가장 작은 값이 그 단계의 결과값이 된다.

dp[i - 1] + 1 : 1을 빼고 최소의 연산 개수를 구하는 경우

dp[i / 2] + 1 : 2로 나누고 최소의 연산 개수를 구하는 경우

dp[i / 3] + 1 : 3으로 나누고 최소의 연산 개수를 구하는 경우

2로 나눠진다면 2로 나눈 경우의 수도 구하고, 3으로 나눠진다면 3으로 나눈 경우의 수를 구해서 그 중 가장 작은 값을

저장하면된다.

'''

from sys import stdin

x = int(stdin.readline())
dp = [0,0,1,1] # 인덱스순서에 맞게 0, 1일때 0 2일떄 1 3일때 1
for i in range(4,x+1):
    dp.append(dp[i-1]+1)
    if i%2 == 0: dp[i] = min(dp[i//2]+1, dp[i])
    if i%3 == 0: dp[i] = min(dp[i//3]+1, dp[i])

print(dp[x])
