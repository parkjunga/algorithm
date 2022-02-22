'''
평균
'''

n = int(input())
arr = list(map(int, input().split()))
m = max(arr)

sum = 0
for j in range(n):
    sum += round(arr[j]/m*100,2)
print(sum/n)