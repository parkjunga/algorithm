import sys

sys.stdin = open("input.txt","rt") # 파일이름, 파일모드(read)

n = int(sys.stdin.readline())
arr = []
# strip이 \n 이다
for _ in range(n):
    word = sys.stdin.readline().strip()
    arr.append(word)
# 거꾸로 :: -1
for i in range(n):
    #print(arr[i][::-1])
    #print(arr[i][0::])
    if arr[i][::-1].lower() == arr[i][0::].lower(): # 거꾸로 불러온다음 소문자끼리 비교
        ans = 'Yes'
    else:
        ans = 'No'
    #print(arr[i][j][0:j+1],end='')
    print('#'+str(i+1),ans)