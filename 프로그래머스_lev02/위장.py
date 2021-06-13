def solution(clothes):
    answer = 0
    # 0번재는 의상의 이름, 1번째는 종류
    answer += len(clothes)
    tmp = {}
    # 나눠서 저장
    for i in range(len(clothes)):
        if clothes[i][1] not in tmp:
            tmp[clothes[i][1]] = []
            tmp[clothes[i][1]].append(clothes[i][0])
        else:
            tmp[clothes[i][1]].append(clothes[i][0])

    if len(tmp.keys()) > 1:
        sum = 1
        for v in tmp.values():
            sum *= len(v)
        answer += sum
    return answer


clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))