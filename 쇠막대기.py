import sys

sys.stdin = open("input.txt","rt") # 파일이름, 파일모드(read)

def solution(n):
    stack = []
    sum = 0
    for i in range(len(n)):
        if n[i] == '(':
            stack.append(n[i])
        else:
            if stack:
                stack.pop()
                if n[i-1] == '(':
                    sum += len(stack)
                    #sum += 2
                else:
                    sum += 1

    print(sum)
n = sys.stdin.readline()

solution(n)