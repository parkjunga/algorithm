def solution(priorities, location):
    answer = 0
    m = max(priorities)
    max_num = 0
    new_l = []
    for i in range(len(priorities)):
        if m == priorities[i] and priorities[location] != m :
            max_num = i
            break
        elif priorities[i] == m:
            answer = 1
            return answer
    if answer == 0:
        for j in range(max_num,len(priorities)):
            new_l.append(priorities[j])
            answer += 1
        for j2 in range(max_num):
            if location == j2:
                answer += 1
            new_l.append(priorities[j2])
        return answer

priorities = [2, 1, 3, 2] # 중요도 순서
location = 2 # 내가 인쇄 요청한 문서 몇 번쟤
solution(priorities,location)

'''
아주 심플

1. 맥스랑 내가 찾고자하는 값이랑 비교했는데 같다 
그러면 1 

2. 맥스랑 내가 찾고자하는 값이랑 다르다 
1 1 9 1 1 1 ( location : 0 )
맥스값 9 로케이션 확인 2일때 앞에 몇개 있나 0,1 

앞과 비교해서 크면 앞에 작으면 맨뒤로 

'''