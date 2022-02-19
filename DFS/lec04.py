'''
1.재귀호출  사용
2.상태트리 사용
'''

def DFS(L, sum): # L은 배열에 인덱스 번호
    if sum > total//2: # 경우의수 추가
        return
    if L == n:
        if sum == (total-sum): # 내가 만든 부분집합의 반대편
            print("yes")
            exit(0)
    else:
        DFS(L+1,sum+a[L]) # 사용 o
        DFS(L+1,sum) # 사용 x

n = int(input()) # 문제에 대한 입력 ex) 6
a = list(map(int,input().split())) # 문제에 대한 입력 ex) 1 3 5 6 7 10
total = sum(a) # 원소에 총합
DFS(0,0)
print("No")