# n 전체 학생의 수
# lost 체육복 도난당한 학생들의 번호가 담긴 배열
# reserve 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열
def solution(n, lost, reserve):
    answer = 0
    n_list = []
    # 먼저 lost와 reserve를 제외한 n에 들어 있는 숫자를 확인
    for i in range(1,n+1):
        if i not in lost and i not in reserve:
            n_list.append(i)

    # 중복숫자는 한개만 카운트됨
    lr = set(lost) & set(reserve)

    if len(lr) > 0:
        for i in list(lr):
            n_list.append(i)
            reserve.remove(i) # 잃어버리고 여유분이 같으면 그 숫자는 여유분에서 제외
            lost.remove(i)
    else: # 이제 reserve에서 lost숫자보다 1크거나 1작은거를 찾아라
        for t in lost:
            for z in reserve:
                if t + 1 == z or t - 1 == z:
                    n_list.append(z)
                    n_list.append(t)
                    reserve.remove(z)
                else:
                    n_list.append(z)

    answer = len(n_list)

    return answer


# 3개의 체육복 중에 앞뒤가 아니기때문에 lost를 빌려줄수없고 따라서 2번
n = 3
lost = [3]
reserve = [1]
print(solution(n,lost,reserve))