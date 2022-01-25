def solution(priorities, location):
    answer = 0
    arr = []
    tmp = 0
    test = {}
    s = max(priorities) # 시작값
    for i in range(len(priorities)):
        if s == priorities[i]:
           tmp = i

    for j in range(tmp,len(priorities)):
        arr.append(priorities[j])
        test[j] = priorities[j]

    for t in range(tmp):
        arr.append(priorities[t])
        test[t] = priorities[t]

    # 최종
    last = []
    for s in test:
        last.append((s,test[s]))

    for j in range(len(last)):
        if last[j][0] == priorities[location]:
            answer = j

    return answer

priorities = [2, 1, 3, 2]	# 중요도 순서
location =  2  # 내가 인쇄 요청한 문서 몇 번쟤

ans = solution(priorities,location)
print(ans)


'''
아주 심플b ? gcd(b,a%b) : a

'''