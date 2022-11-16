# 괄호문제 스택이용?
'''
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
'''

def solution(str):
    answer = 'NO'
    stack = []

    for i in range(len(str)):
        if str[i] == '(':
            stack.append(str[i])
        elif str[i] == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                return answer
                break
    if len(stack) == 0:
        answer = 'YES'
    return answer

n = int(input())

for i in range(n):
    print(solution(input()))


