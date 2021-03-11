from sys import stdin

def soulution(m,arr):
    cnt = 0
    for i in range(len(arr)):
        if m == arr[i]:
            cnt += 1

    return cnt

n = int(stdin.readline())
n_arr = list(map(int,stdin.readline().split()))
m = int(stdin.readline())
m_arr = list(map(int,stdin.readline().split()))
stack = []

for i in range(m):
    cnt = soulution(m_arr[i],n_arr)
    stack.append(cnt)
ans = ' '.join(map(str,stack))
print(ans)