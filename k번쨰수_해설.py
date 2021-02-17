import sys

sys.stdin = open("input.txt","rt") # 파일이름, 파일모드(read)

T = int(input())

# 케이스 갯수만큼 돌아야됨
for t in range(T):
    n,s,e,k = map(int,input().split()) # 읽어들이면서 매핑
    # 리스트로 넣기
    a = list(map(int,input().split()))

    # ~번쨰부터니까
    # s번째부터 e까지니까
    a=a[s-1:e] #s번째 인덱스는 0부터 시작하니까
    a.sort()

    # k번째 출력하라니까 0,1,2,3,4 => 1,2,3,4,5 니까 -1 을 해줘야됨됨
    print("#%d %d" %(t+1,a[k-1]))

