def solution(s):
    stack = []
    answer = []
    for i in s:
        if i not in stack:
            stack.append(i)
            answer.append(-1)
        else:
            print(stack.index(i))
            answer.append(i)
    return answer


s = "banana"

print(solution(s))