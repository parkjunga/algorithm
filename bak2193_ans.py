'''
규칙잦기
n = 1  1  -> 1개
n = 2  10  -> 1개
n = 3  1 00 ..

n = (n -1) + (n-2)
'''

from sys import stdin
n = int(stdin.readline())
dp = [0,1,1] # 0번째 0개 1번째 1개 2번째 1개
for i in range(3,n+1): # 3번째 값부터
    dp.append(dp[i-1] + dp[i-2])
print(dp[n])