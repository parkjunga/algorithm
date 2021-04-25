'''
문자열 s : 1개 이상 단어
각 단어 : 하나 이상의 공백 문자로 구분
각 단어의 짝수 : 대문자
''       홀수 : 소문자
'''

def solution(s):
    new = s.split(' ')
    list = []
    for i in range(len(new)):
        answer = ''
        for j in range(len(new[i])):
            if j % 2 == 0:
                answer += new[i][j].upper()
            else:
                answer += new[i][j].lower()
        list.append(answer)
    answer = ' '.join(list)
    return answer

s = "try hello world"
print(solution(s))

