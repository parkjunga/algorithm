def solution(s):
    answer = 0
    stack = []
    # 먼저 s에 0번째 자리수를 넣어놓는다.
    stack.append(s[0])
    for i in range(1,len(s)):
        # list에 인덱스 부족하다는 에러 방지를 위해 아예 비었을 경우엔 값을 넣는다.
        if len(stack) == 0:
            stack.append(s[i])
        else:
            # 그게 아니라면 맨뒤에 값이랑 현재 값이랑 같은지 비교하고 같으면 삭제
            if stack[-1] == s[i]:
                stack.pop()
            else:
                # 아니면 추가해준다.
                stack.append(s[i])
    # 전체 스택이 비었으면 모두 같다. 
    if len(stack) == 0:
        answer = 1
    return answer



s = 'cdcd'
print(solution(s))