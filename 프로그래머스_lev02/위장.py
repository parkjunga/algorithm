
def solution(clothes):
    answer = 1
    dic = {}

    # 딕셔너리에 분류
    for i in range(len(clothes)):
        if clothes[i][1] in dic.keys():
            dic[clothes[i][1]].append(clothes[i][0])
        else:
            dic[clothes[i][1]] = []
            dic[clothes[i][1]].append(clothes[i][0])
            dic[clothes[i][1]].append('none') # 안입는 경우의 수 (포함되지 않는갯수

    # 경우의수 구하기
    for i in dic.values():
        answer *= len(i)
    answer = answer-1 # 안입는 경우의 수 제거 (하나씩 입지않아도되니까
    return answer

clothes = [["동그란안경", "얼굴"], ["검정선글라스", "얼굴"], ["파란색셔츠", "상의"],["파란색셔츠", "하의"],["코트","겉옷"]]
print(solution(clothes))