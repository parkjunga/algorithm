# -*- coding: utf-8 -*-
def solution(table, languages, preference):
    answer = ''

    # 1. 가장먼저 문자열을 배열로 만들 배열 선언
    arr = [[] for i in range(len(table))]
    # 2, 직업군 언어 점수를 담는 딕셔너리 선언
    jumsu = {
        'SI' : 0,
        'CONTENTS':0,
        'HARDWARE':0,
        'PORTAL':0,
        'GAME':0
    }
    # 3.마지막으로 알파벳순으로 가장 작으면서 맥스값을 비교해서 넘길 딕셔너리 선언
    dic = {}

    # 4. 문자열을 2차원 배열로 담는다.
    for i in range(len(table)):
        arr[i] = table[i].split()

    # 5. 값을 가공 시작
    for i in range(len(arr)):
        sum = 0
        arr[i] = list(reversed(arr[i]))
        # 6. 직업군 언어 점수별로 값 가져오기
        for j in range(len(arr)):
            # 7.비교
            if arr[i][j] in languages:
                # 언어 선호도를 통해 값 계산
                for t in range(len(preference)):
                    if arr[i][j] == languages[t]:
                        sum += preference[t] * (j+1)
        jumsu[arr[i][5]] = sum
    answer = (max(jumsu.keys(), key=lambda k : jumsu[k]))

    # 마지막으로 가장 큰값과 같은 key를 불러온다
    for key,value in jumsu.items():
        if value == max(jumsu.values()):
            dic[key] = ord(key[0]) # 같은값들의 아스키코드값을 새로운 딕셔너리에 담는다.
    answer = (min(dic.keys(), key=lambda k : dic[k]))
    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]
ans = solution(table, languages, preference)
print(ans)