def solution(priorities, location):
    answer = 0
    dub = {}
    for i in range(len(priorities)):
        dub[i] = priorities[i]

    # sorting
    max_key = max(dub,key=dub.get)
    max_value = max(dub.values())
    new_temp = {}
    for i in range(max_key,len(priorities)):
        new_temp[i] = priorities[i]
    for j in range(max_key):
        new_temp[j] = priorities[j]
    print(new_temp)
    # 마지막 정렬
    i = 0
    for k,v in new_temp.items():
        i += 1
        if k == location:
            answer = i

    return answer


priorities = [1,2,8,3,4]
location = 4

print(solution(priorities,location))