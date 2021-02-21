
import sys

sys.stdin = open("input.txt","rt") # 파일이름, 파일모드(read)

N, K = map(int,sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
#print(arr)
# 중복 제거를 먼저해야됨
res=set()

'''
삼중for문
i j m m m 
1 2 3 4 5
1 + 2 + 3
1 + 2 + 4
1 + 2 + 5 ..

j 가 3일때 ...
1 + 3 + 4 
1 + 3 + 5 

'''

# 자료를 뽑아서 합해야됨 중복을 방지하기위해서
for i in range(N):
    for j in range(i+1,N): # i뒤에자료 선택
        for m in range(j+1,N): # j뒤편부터 돌아야됨
            res.add(int(arr[i])+int(arr[j])+int(arr[m])) # 중복을 제거하면서 set에 입력됨

# sort를 위해 list화
res= list(res)
res.sort(reverse=True)
print(res[K-1])