from collections import deque


def solution(priorities, location):
    answer = 0
    d = deque([(v,i) for i,v in enumerate(priorities)])
    # value값 인덱스값 저장
    while len(d):
        item = d.popleft() # j  맨앞값
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0

ans = solution(priorities,location)
print(ans)