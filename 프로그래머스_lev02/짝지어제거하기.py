'''
중복제거
1. 스택을 이용 tmp 리스트만들기
2. 비었을 경우에 무조건 넣고
3. 넣은값과 들어오는 값비교해서 같으면 제거
4. 아닉면 다시 넣고
'''

def solution(s):
    answer = 0
    tmp = []
    for i in s:
        if len(tmp) == 0:
            tmp.append(i)
        elif i == tmp[-1]:
            tmp.pop()
        else:
            tmp.append(i)
    if len(tmp) == 0:
        answer = 1
    return answer


s= 'cdcd'
print(solution(s))