def solution(s):
    answer = True
    # 스택으로 풀면됨
    arr = []
    for i in range(len(s)):
        if '(' == s[i]:
            arr.append(s[i])
        else:
            if len(arr) == 0:
                answer = False
            else:
                arr.pop()
    if len(arr) == 0:
        return answer
    else:
        answer = False
        return answer

