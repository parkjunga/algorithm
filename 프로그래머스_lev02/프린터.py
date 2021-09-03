def solution(priorities, location):
    answer = 0
    new = list(enumerate(priorities))
    # 거꾸로 + 순서
    test = sorted(new,key=lambda x: (-x[1]))
    #print(test[0][0])
    stack = []
    stack.append(test[0][0])
    for i in range(len(test)):
        if stack[0] < test[i][0]:
            stack.append(test[i][0])
    for j in range(len(test)):
        if test[j][0] not in stack:
            stack.append(test[j][0])

    for t in range(len(stack)):
        if stack[t] == location:
            answer = t+1
    return answer

priorities = [1,1,9,1,1,1] # 중요도 순서
location = 0 # 내가 인쇄 요청한 문서 몇 번쟤

solution(priorities,location)



'''
아주 심플b ? gcd(b,a%b) : a

'''