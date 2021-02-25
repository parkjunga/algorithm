import sys

sys.stdin = open("input.txt","rt") # 파일이름, 파일모드(read)

s = input()
stack = []
cnt = 0 # 카운팅값

for i in range(len(s)):
    # 여는 괄호일경우 append
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(': # 레이져
            cnt += len(stack) # 스택의 길이 열어야되는것 (쇠막대기)
        else:
            # 닫는괄호라 
            cnt += 1 # 막대기 카운팅
    print(cnt)

